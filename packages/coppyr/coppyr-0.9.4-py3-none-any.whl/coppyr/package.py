# -*- coding: utf-8 -*-
import os
import io
import itertools
import shutil
import sys

from typing import List, Dict

from setuptools import Command
from pip._internal.req import parse_requirements as pip_parse_requirements


def get_readme(fname="README.md", path=os.getcwd()):
    path = os.path.join(path, fname)
    with io.open(path, encoding="utf-8") as f:
        return "\n" + f.read()


class UploadCommand(Command):
    """
    Support setup.py upload.

    NOTE: This upload command requires `twine` to upload to PyPI.  See an
    example usage via NGINX Crossplane:

    https://github.com/nginxinc/crossplane/blob/master/setup.py#L92
    """

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print(f'\033[1m{s}\033[0m')

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds...")
            shutil.rmtree(os.path.join(os.getcwd(), "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution...")
        os.system(f"{sys.executable} -m build")

        self.status("Uploading the package to PyPI via Twine...")
        os.system("twine upload dist/*")

        sys.exit()


def parse_requirements(fpath: str) -> List[str]:
    requirements = []

    for req in pip_parse_requirements(fpath, session="tmp"):
        if hasattr(req, "req"):
            requirements.append(str(req.req))
        else:
            requirements.append(str(req.requirement))

    return requirements


def parse_extras(**kwargs: str) -> Dict[str, List[str]]:
    """
    Parse a key-value pairing of extras keys and file paths and return a dict
    which can be passed to setup.py as "extras_require".

    This logic will automatically include an "all" extras argument which will
    include all extras parsed by this func.  It will exclude the "dev" key from
    this "all" tag.

    https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#optional-dependencies
    """
    extras_dict = {
        k: parse_requirements(v)
        for k, v in kwargs.items()
    }

    extras_dict["all"] = list(
        itertools.chain(
            *[v for k, v in extras_dict.items() if k != "dev"]
        )
    )

    return extras_dict
