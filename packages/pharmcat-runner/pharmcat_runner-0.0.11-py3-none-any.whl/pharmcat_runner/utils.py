# MIT License

# Copyright (c) 2024 Andrew Haddad

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import glob
import logging
import os
import shutil
import subprocess
import tarfile

from functools import wraps
from .common import *


def log(logger):
    def middle(func):
        @wraps(func)
        def logged(*args, **kwargs):
            result = func(*args, **kwargs)
            # func_name_fmtd = format_func_name(func=func)
            try:
                inputs = args[0]
            except IndexError:
                inputs = kwargs[0]
            finally:
                msg_fmtd = f"{func.__module__}:Completed {func.__name__} with input `{inputs}` and output `{result}`"
            logger.info(msg_fmtd)
            return result

        return logged

    return middle


def create_logger(
    name, log_level=logging.INFO, stream=False, file="pharmcat_runner.log"
):
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    file_handler = logging.FileHandler(file)
    logger.addHandler(file_handler)
    if stream:
        stream_handler = logging.StreamHandler()
        logger.addHandler(stream_handler)
    for handler in logger.handlers:
        handler.setLevel(log_level)
        handler.setFormatter(logging.Formatter(LOGGING_FORMAT))
    return logger


def format_func_name(func):
    func_name_fmtd = []
    for i, name in enumerate(func.__name__.split("_")):
        if i == 0:
            if name != "split":
                name = name + "ed"
        func_name_fmtd.append(name)
    return " ".join(func_name_fmtd)


def blockgz_compress(input_file, output_file):
    run_command(f"bgzip -ck {input_file} > {output_file}", shell=True)
    return output_file


def get_files(dir_):
    try:
        files = []
        filenames = os.listdir(dir_)
        for file in filenames:
            files.append(os.path.join(dir_, file))
    except FileNotFoundError:
        files = glob.glob(dir_)
    return files


def validate_environment():
    # Don't need to check for pharmcat or reference genome as these
    # would be installed by the pharmcat_pipeline if they don't already
    # exist
    tools = [
        "bcftools",
        "tabix",
        "plink",
        os.path.join(os.environ.get("JAVA_HOME"), "bin", "java"),
    ]
    for tool in tools:
        try:
            if tool == "bcftools":
                args = [tool, "-v"]
            else:
                args = [tool, "--version"]
            output = run_command(args, capture_output=True)
        except Exception:
            raise RuntimeError(f"Unable to validate existence of {tool}")
        if tool in {"bcftools", "tabix"}:
            version = output.split("\n")[0].split()[-1].split(".")
            version_suffix = int(version[-1])
            if version_suffix < 18:
                raise RuntimeError(
                    f"Version of {tool} must be >= {HTS_LIB_REQUIRED_VERSION}. Found {version}"
                )
    if not os.path.exists(BIN_DIR):
        raise RuntimeError("Unable to find pharmcat installation.")
    for file in os.listdir(BIN_DIR):
        if "preprocessor" in file:
            break
    else:
        raise RuntimeError("Unable to find preprocessor installation.")


def run_command(args, shell=False, capture_output=False):
    stdout = subprocess.run(args, capture_output=True, text=True, shell=shell)
    check_stdout(stdout)
    if capture_output:
        return stdout.stdout


def check_stdout(stdout):
    if stdout.returncode != 0:
        raise RuntimeError(
            f"Error running command {stdout.args} with error: {stdout.stderr}"
        )


def curl(dir_, url):
    run_command(f"cd {dir_} && curl -OL {url}", shell=True)


def unpack_tar(file, dir_="."):
    with tarfile.open(file) as f:
        f.extractall(path=dir_)


def maybe_create_dir(dir_, strict=False):
    if strict:
        try:
            shutil.rmtree(dir_)
        except FileNotFoundError:
            pass
    if not os.path.exists(dir_):
        os.mkdir(dir_)


def validate_directory(dir_, file_ext=None):
    if not isinstance(dir_, str):
        raise TypeError(f"Directory must be a string, got '{type(dir_)}'")
    glob_files = glob.glob(dir_)
    globbing = True
    for file in glob_files:
        if file_ext in file:
            break
    else:
        globbing = False
    if not globbing and len(os.listdir(dir_)) == 0:
        raise ValueError(
            f"Provided directory '{dir_}' does not exist or does not contain any files"
        )


def check_python_verison():
    version_data = sys.version
    if int(version_data.split()[0].split(".")[1]) >= 9:
        return True
    return False


def validate_plink():
    try:
        run_command(["plink", "-h"])
    except RuntimeError:
        raise RuntimeError(
            "PLINK was not found. Must install PLINK to run sample call rate or Hardy-Weinburg QC steps."
        )


def validate_file(file):
    if not isinstance(file, str):
        raise TypeError(f"File path must be a string, got '{type(file)}'")

    if not os.path.exists(file):
        raise FileNotFoundError(f"File '{file}' does not exist")

    if not os.path.isfile(file):
        raise FileNotFoundError(f"Path '{file}' is not a file")

    if not os.access(file, os.R_OK):
        raise PermissionError(f"File '{file}' is not readable")
