# -*- coding: utf-8 -*-
import subprocess
from logging import Logger

from typing import ByteString, List, Optional, Tuple, TextIO, Union

from coppyr.error import CoppyrError


class CoppyrSubpError(CoppyrError):
    description = "An error occurred durring subp.call"


def call(
    command: str,
    check: bool=True,
    raw: bool=False,
    fg: bool=False,
    input: Optional[str]=None,
    stdin: Optional[TextIO]=None,
    stdout: Optional[TextIO]=None,
    stderr: Optional[TextIO]=None,
    log: Optional[Logger]=None
) -> Union[
    Tuple[int, List[str], List[str]],
    Tuple[int, ByteString, ByteString]
]:
    """
    Calls subprocess.run with the pass command.

    :param command: String
        Full shell command
    :param check: Boolean
        Check the return code or not
    :param raw: Boolean
        Flag to return raw outputs or not
    :param fg: Boolean
        Flag to indicate whether or not the command should be run in
        the foreground.
    :param input: String
        String input to send via stdin/communicate to the process.
    :param stdin: File-like object
        stdin to passthrough to the subprocess.  Default is
        subprocess.PIPE.
    :param stdout: File-like object
        stdout to passthrough to the subprocess.  Default is
        subprocess.PIPE.
    :param stderr: File-like object
        stderr to passthrough to the subprocess.  Default is
        subprocess.PIPE.
    :param log: logging.Logger
        Logger to send log entries to.  Can be `None` to disable logging.
        Disabled by default.
    :return: retcode int, stdout [], stderr []
    """
    subprocess_params = dict(
        shell=True
    )

    if not fg:
        stdin = subprocess.PIPE if stdin is None else stdin  # type: ignore
        stdout = subprocess.PIPE if stdout is None else stdout  # type: ignore
        stderr = subprocess.PIPE if stderr is None else stderr  # type: ignore

        subprocess_params.update(dict(  # type: ignore
            stdin=stdin,
            stdout=stdout,
            stderr=stderr
        ))

    if input:
        if 'stdin' in subprocess_params:
            del subprocess_params['stdin']
        subprocess_params['input'] = input  # type: ignore

    if log is not None:
        log.debug(f"coppyr.subp.call: Calling \"{command}\"")

    process = subprocess.run(command, **subprocess_params)

    try:
        if process.returncode != 0 and check:
            if log is not None:
                log.error(
                    f"piston.subp.call: \"{command}\" returned a non-zero "
                    f"exit code \"{process.returncode}\""
                )

            raise CoppyrSubpError(
                message=f"\"{command}\" returned a non-zero exit code.",
                payload=dict(returncode=process.returncode)
            )
        elif fg:
            return process.returncode, [], []
        elif raw:
            return process.returncode, process.stdout, process.stderr
        else:
            # out, err are bytes objects
            out = process.stdout.decode("utf-8").split('\n')
            err = process.stderr.decode("utf-8").split('\n')

            if log is not None:
                if out:
                    log.debug("coppyr.subp.call: stdout:\n" + "\n".join(out) + "\n")
                if process.stderr:
                    log.error("coppyr.subp.call: stderr:\n" + "\n".join(err) + "\n")

            return process.returncode, out, err
    except CoppyrSubpError:
        raise
    except Exception as e:
        if log is not None:
            log.error(
                f"coppyr.subp.call: Caught \"{e.__class__.__name__}\" during "
                "subp.call."
            )

        raise CoppyrSubpError(
            f"Caught \"{e.__class__.__name__}\" during subp.call.",
            payload={"command": command},
            caught=e
        )
