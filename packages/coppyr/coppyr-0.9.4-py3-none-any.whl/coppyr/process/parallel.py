import multiprocessing as mp
import queue as q
import sys
import uuid

from coppyr.types.singleton import Singleton


class Worker(object):
    """
    This is a utility wrapper for taking a function and converting it into a
    callable that accepts Queue pipes from Parent process rather than direct
    inputs.
    """
    def __init__(self, func, input_type="args", name=None, logger=None):
        self.func = func
        self.input_type = input_type
        self.name = name or str(uuid.uuid4())[:8]
        self.logger = logger

    def __call__(self, input_queue, result_queue):
        # disable logging from dependencies as logging in Python is not process safe
        import logging
        logging.disable(logging.CRITICAL)

        while True:
            # get an input
            try:
                inp = input_queue.get(timeout=10)
            except q.Empty as e:
                if self.logger is not None:
                    self.logger.info(f"[parallel.Worker {self.name}] Queue get timed out")
                continue

            # This will block until an item is retrieved from the queue
            # the queue.
            # https://docs.python.org/3.6/library/multiprocessing.html#multiprocessing.Queue

            # to kill a process, put None into the queue
            if inp is None:
                # print(f'Closing worker {self.name}')
                break
            try:
                if self.input_type == "arg":
                    result = self.func(inp)
                elif self.input_type == "args":
                    result = self.func(*inp)
                elif self.input_type == "kwargs":
                    result = self.func(**inp)
                elif self.input_type == "mixed":
                    result = self.func(
                        *inp.get("args", []),
                        **inp.get("kwargs", {})
                    )
                else:
                    raise TypeError(f"Unrecognized input type \"{self.input_type}\"")
            except Exception as e:
                _, _, tb = sys.exc_info()
                result = e.with_traceback(tb)
                result_queue.put(result)
            else:
                result_queue.put(result)


class Pool(object):
    """
    Class that spawns a group of workers and can send work / receive results
    from that group.  This allows us to keep workers alive (and their state)
    in between workloads.

    BUYER BE WARNED...This module worked at one point quite well for farming
    out local processing, but recently when trying to make use of it in a
    Google Function inter process communication was very unstable.  There is
    likely some work to be done to shore this utility area up before it is
    ready for prime time.

    Also, consider a rework to use concurrent.Futures as an alternative now in
    Python 3.  Under the covers that stdlib uses multiprocessing primatives for
    Process executors, but perhaps it is a bit more user friendly.
    """
    def __init__(self, func, size=4, input_type="args", manager=None,
                 name=None, logger=None):
        # https://stackoverflow.com/questions/43439194/python-multiprocessing-queue-vs-multiprocessing-manager-queue/45236748#45236748
        # https://docs.python.org/3/library/multiprocessing.html#multiprocessing-managers
        if manager is None:
            # hold reference open to prevent gc if self-managed
            self.manager = mp.Manager()
            # If we don't do this then the manager might be GC'd at any time
            # and once that happens its queue proxies will not be usable.  We
            # don't have to do it for externally passed managers because we
            # implicitly trust that instantiating logic will hold open a
            # reference to prevent GC for us.

            manager = self.manager

        self.sent = manager.Value(int, 0)
        self.input_queue = manager.Queue()
        self.result_queue = manager.Queue()
        self.name = name or str(uuid.uuid4())[:8]
        self.logger = logger

        self.workers = [
            mp.Process(
                target=Worker(func, input_type, name=f"{self.name}_{i}", logger=self.logger),
                args=(self.input_queue, self.result_queue),
                daemon=True,
                name=f"{self.name}_{i}"
            )
            for i in range(size)
        ]

        # start the workers
        for process in self.workers:
            process.start()

    @property
    def waiting(self):
        """
        Boolean indicator showing whether or not there is still work queued.
        """
        return not self.input_queue.empty()

    @property
    def empty(self):
        """
        Boolean indicator showing whether or not there are result messages
        available.
        """
        return self.result_queue.empty()

    @property
    def idle(self):
        """
        Use our self tracked message counter to indicate whether or not the
        pool has outstanding work, doing work, or has results that haven't been
        handled.
        """
        return self.sent.value == 0

    def send(self, *args):
        """
        Send tasks to the pool.  Returns the count of tasks sent.
        """
        current = 0
        for inp in args:
            self.input_queue.put(inp)
            self.sent.value += 1
            current += 1

        return current

    def recv(self, timeout=None):
        result = self.result_queue.get(timeout=timeout)
        self.sent.value -= 1
        return result

    def results(self, timeout=None):
        """
        Read results from children, this will block until we receive responses
        for each message sent
        """
        results = []

        for _ in range(self.sent.value):
            try:
                results.append(self.recv(timeout=timeout))
            except q.Empty as e:
                results.append(e)
                break

        return results

    def run(self, *args):
        # if there is outstanding work in the input queue, don't execute since
        # we can't guarantee the results are from this run call
        if self.sent.value != 0:
            return []

        self.send(*args)

        # return results
        return self.results()

    def stop(self):
        # clean up workers (in case signaled close didn't get all of them)
        # print('Terminating worker processes')
        for process in self.workers:
            if process.is_alive():
                process.terminate()

        # print('Resetting worker pool and queues')
        self.workers = []  # just for good measure deallocate for GC

        # This isn't strictly necessary, but making sure that workers are
        # cleaned up before the queues will avoid raising EOF errors in
        # workers.  (EOF happens if queue is closed before the workers exit)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # https://docs.python.org/3/reference/datamodel.html#object.__exit__
        self.stop()

    def __del__(self):
        # NOTE: __del__ is not reliably called by the GC so anything that we
        # want to make SURE runs shouldn't go here.
        self.stop()


class LogHandler(object):
    """
    Alternative worker implementation that initializes logging in the forked
    process and handles remote log structure message from the Logging pool.
    """
    def __call__(self, input_queue, result_queue):
        from coppyr.context import Context
        context = Context()
        logger = context.log

        while True:
            try:
                # get an input
                inp = input_queue.get(timeout=5)
            except q.Empty as e:
                continue

            # handle special increment message
            if isinstance(inp, str) and inp == "inc_action_id":
                context.inc_action_id()
                result_queue.put(None)
                continue

            level, msg = inp.get("args", ("error", "Malformed remote log payload"))
            kwargs = inp.get("kwargs", {})

            try:
                # log the message (e.g. logger.error("my message", exc_info=True))
                getattr(logger, level)(msg, **kwargs)
            except AttributeError:
                logger.error(f"Invalid logging level: \"{level}\"")

            # just send an empty result to indicate message handling
            result_queue.put(None)


class Logger(Pool, Singleton):
    """
    A multiprocessing-safe logger.  This is a process pool which spawns a
    (SINGLE) separate process that will be responsible for log handling.  Log events are
    converted into tuples which are then logged by the separate process.
    """
    def __init__(self, manager, level):
        # manager is required because we need this pool to be picklable
        self.level = level

        # basically init an empty pool
        super().__init__(lambda: True, size=0, manager=manager)

        self.workers.append(
            mp.Process(
                target=LogHandler(),
                args=(self.input_queue, self.result_queue),
                daemon=True,
                name="parallel.logger"
            )
        )

        # start the logger
        self.workers[-1].start()

    def inc_action_id(self):
        """
        Send special message which increments the remote action id
        """
        self.send("inc_action_id")

    def critical(self, msg, **kwargs):
        self.send({"args": ("critical", msg), "kwargs": kwargs})

    def error(self, msg, **kwargs):
        self.send({"args": ("error", msg), "kwargs": kwargs})

    def warning(self, msg, **kwargs):
        self.send({"args": ("warning", msg), "kwargs": kwargs})

    def info(self, msg, **kwargs):
        self.send({"args": ("info", msg), "kwargs": kwargs})

    def debug(self, msg, **kwargs):
        self.send({"args": ("debug", msg), "kwargs": kwargs})


def run(func, inputs, n=4, input_type="args"):
    """
    Take a function and parallelize it.  This is a thin utility for
    experimentation purposes.

    :param func: Callable
        Function to call in child processes.
    :param inputs:  Iterable[Tuple|List|Dict]
        Iterable of inputs that you want to pass to the remote functions.
    :param n: Integer
        Number of children you want to spawn.
    :param input_type: String ["arg" | "args" | "kwargs"]
        Whether or not the passed inputs are args (ordered) or kwargs (key-word
        arguments).  This dictates how the inputs are expanded when calling the
        function.
    :return: List
        List of results that were returned by child workers.
    """

    exec_pool = Pool(func, size=n, input_type=input_type)

    # send the work to the Pool
    results = exec_pool.run(*inputs)

    exec_pool.stop()

    # return results
    return results
