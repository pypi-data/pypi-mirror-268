import asyncio

from coppyr.collections import DotDict


class Loop:
    def __init__(self, new_event_loop=False):
        if new_event_loop:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        self.event_loop = asyncio.get_event_loop()
        self.tasks = set()
        self.results = []
        self.queues = DotDict()

    def task_complete(self, coroutine):
        self.tasks.discard(coroutine)
        self.results.append(coroutine.result())

    def create_task(self, coroutine, *args, **kwargs):
        # create the task
        task = self.event_loop.create_task(coroutine, *args, **kwargs)

        # add the tasks to tracking
        self.tasks.add(task)

        # on done, have the task remove itself
        task.add_done_callback(self.task_complete)

    def run_until_complete(self):
        self.event_loop.run_until_complete(asyncio.wait(self.tasks))

    def run_forever(self):
        self.event_loop.run_forever()

    def stop(self):
        self.event_loop.stop()

    def close(self):
        self.event_loop.close()

    def create_queue(self, name, maxsize=0):
        self.queues[name] = asyncio.Queue(maxsize=maxsize)
        return self.queues[name]

    def current_task(self):
        return asyncio.current_task()

    def is_running(self):
        return self.event_loop.is_running()

    def is_closed(self):
        return self.event_loop.is_closed()

