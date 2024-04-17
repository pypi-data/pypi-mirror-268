"""任务基础类"""
import shutil
import subprocess
import inspect
import os
import sys
import tempfile
import shlex
from lbkit.log import Logger
from lbkit import errors
from lbkit import misc
from lbkit.misc import Color


class Tools(object):
    """基础工具类"""
    def __init__(self, log_name: str):
        os.makedirs(misc.LOG_DIR, exist_ok=True)
        self.log_name = os.path.join(misc.LOG_DIR, f"{log_name}.log")
        self.log: Logger = Logger(log_name)

    @staticmethod
    def _real_command(shell: str):
        if not isinstance(shell, str):
            raise errors.ArgException("Command {} must be string, get: {}".format(shell, type(shell)))
        cmd = shlex.split(shell)
        if len(cmd) == 0 or len(cmd[0].strip()) == 0:
            raise errors.ArgException("Command is empty")
        for c in cmd:
            if not isinstance(c, str):
                raise errors.ArgException("Command {} with type error, must be string, get: {}"
                                          .format(c, type(shell)))
        if cmd[0].find("./") >= 0:
            raise errors.ArgException("Command {} can't be relative path")
        which_cmd = shutil.which(cmd[0])
        if which_cmd is None:
            raise errors.NotFoundException(f"Command {cmd[0]} not found")
        cmd[0] = which_cmd
        if cmd[0] == shutil.which("sudo"):
            raise errors.ArgException("Can't run command with sudo, get: {}".format(shell))
        return cmd

    def exec(self, cmd: str, verbose=False, ignore_error = False, sensitive=False, log_prefix=""):
        """执行命令"""
        stack = inspect.stack()[1]
        file = os.path.basename(stack.filename)
        line = stack.lineno

        show_cmd = "***" if sensitive else cmd
        if log_prefix:
            show_cmd = "(" + log_prefix + ") " + show_cmd

        fd = os.fdopen(os.open(self.log_name, os.O_APPEND | os.O_CREAT | os.O_RDWR), "a+")
        self.log.debug("{}>>>>{} {}".format(Color.GREEN, Color.RESET_ALL, show_cmd))
        fd.write(">>>> {}".format(show_cmd))
        if os.environ.get("VERBOSE", False):
            verbose = True
        real_cmd = self._real_command(cmd)
        result = subprocess.Popen(real_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        if result is None:
            raise errors.RunCommandException(f"Run command {real_cmd[0]} failed")
        for msg in result.stdout:
            fd.write(msg)
            if verbose:
                sys.stdout.write(msg)
        fd.close()
        result.communicate()
        if result is None or result.returncode != 0:
            self.log.error(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            msg = f"{file}:{line} > Run command failed, cmd: {show_cmd}, error code: {result.returncode}, log: {self.log_name}"
            if not ignore_error:
                raise errors.RunCommandException(msg)
            self.log.error(msg)
        return result

    def pipe(self, cmds: list[str], ignore_error=False, out_file = None):
        if not isinstance(cmds, list):
            raise errors.ArgException("Command ({}) with type error, only list[str] can be accepted".format(cmds))
        stdin = None
        for cmd in cmds:
            self.log.debug("{}>>>>{} {}".format(Color.GREEN, Color.RESET_ALL, cmd))
            stdout = tempfile.TemporaryFile("w+b")
            real_cmd = self._real_command(cmd)
            ret = subprocess.Popen(real_cmd, stdout=stdout, stdin=stdin)
            if ret is None:
                raise errors.RunCommandException(f"Run command {real_cmd[0]} failed")
            ret.communicate()
            if ret is None or ret.returncode != 0:
                if ignore_error:
                    self.log.info("Run command ({}) failed".format(cmd))
                    return
                raise errors.RunCommandException()
            if stdin:
                stdin.close()
            stdin = stdout
        if out_file:
            stdin.seek(0)
            with open(out_file, "w+b") as fp:
                fp.write(stdin.read())
        stdin.close()

    def run(self, cmd, ignore_error=False):
        self.log.debug("{}>>>>{} {}".format(Color.GREEN, Color.RESET_ALL, cmd))
        real_cmd = self._real_command(cmd)
        check = False if ignore_error else True
        return subprocess.run(real_cmd, capture_output=True, check=check, encoding="utf-8")

