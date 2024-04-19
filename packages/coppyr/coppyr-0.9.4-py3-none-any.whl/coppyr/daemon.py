import time

from daemon.runner import DaemonRunner

from coppyr.context import Context


# When running in a daemon context we _need_ context to be setup to
# appropriately pass the right values to os.fork().
context = Context()
context.setup()


class Runner(DaemonRunner):
    # See source code here: https://pagure.io/python-daemon/
    def __init__(self, app):
        super().__init__(app)

        self.app = app

        # daemon context modifications
        # https://pagure.io/python-daemon/blob/main/f/daemon/daemon.py#_108
        self.daemon_context.detach_process = getattr(
            self.app, "detach_process", None
        )
        self.daemon_context.files_preserve = getattr(
            self.app,
            "files_preserve",
            context.get_file_handlers()
        )
        self.daemon_context.signal_map = getattr(self.app, "signal_map", {})

    def _open_streams_from_app_stream_paths(self, app):
        # Ugly hack to fix a bug where DaemonRunner can't open stdin and stdout
        # in "w+t" mode (text w+).  This seems to be a Python 3 thing...see
        # more information here: https://bugs.python.org/issue20074
        self.daemon_context.stdin = open(app.stdin_path, "rt")
        self.daemon_context.stdout = open(app.stdout_path, "w+b", buffering=0)
        self.daemon_context.stderr = open(app.stderr_path, "w+b", buffering=0)


class App:
    def __init__(self):
        super().__init__()

        global context
        self.context = context

        # daemon app attributes
        self.pidfile_path = f"/tmp/{self.context.app_name}.pid"
        self.pidfile_timeout = 5
        self.stdin_path = "/dev/null"
        self.stdout_path = "/dev/stdout"
        self.stderr_path = "/dev/stderr"

        # daemon context settings
        self.detach_process = None
        self.files_preserve = context.get_file_handlers()
        self.signal_map = {}
        # Example signal handling:
        # self.daemon_context.signal_map = {
        #     signal.SIGTERM: callable<(signum, frame)>
        # }
        # See IRL example here:
        # https://github.com/nginxinc/nginx-amplify-agent/blob/master/amplify/agent/common/runner.py#L25

    def run(self):
        while True:
            print("Default daemon is running...sleeping")
            time.sleep(60)
