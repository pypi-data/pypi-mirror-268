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

import os
import shutil
import sys
import traceback
from tempfile import TemporaryDirectory

from .common import *
from .utils import curl, run_command, unpack_tar, check_python_verison, create_logger


logger = create_logger(__name__, stream=True)


def install_java(tempdir):
    curl(tempdir, JAVA_URL)
    unpack_tar(file=os.path.join(tempdir, os.path.basename(JAVA_URL)), dir_=BIN_DIR)


def install_python(tempdir):
    curl(tempdir, PYTHON_URL)
    unpack_tar(file=os.path.join(tempdir, os.path.basename(PYTHON_URL)), dir_=tempdir)
    python_dir = os.path.basename(PYTHON_URL).replace(".tgz", "")
    python_dir_current = os.path.join(tempdir, python_dir)
    run_command(
        f"cd {python_dir_current} && ./configure --prefix={os.path.join(BIN_DIR, 'python')}",
        shell=True,
    )
    run_command(f"cd {python_dir_current} && make", shell=True)
    run_command(f"cd {python_dir_current} && make altinstall", shell=True)


def install_pharmcat():
    dir_ = os.path.join(BIN_DIR, "preprocessor")
    curl(dir_, PHARMCAT_JAR_URL)
    os.rename(
        os.path.join(dir_, os.path.basename(PHARMCAT_JAR_URL)),
        os.path.join(dir_, "pharmcat.jar"),
    )


def download_reference_genome(tempdir):
    curl(dir_=tempdir, url=REFERENCE_GENOME_URL)
    unpack_tar(
        file=os.path.join(tempdir, os.path.basename(REFERENCE_GENOME_URL)),
        dir_=os.path.join(BIN_DIR, "preprocessor"),
    )


def install_preprocessor(tempdir):
    # TODO resolve pipenv/dependency issue on MAC; works on linux
    # version = re.findall(r"\d\.\d+", os.path.basename(PYTHON_URL))[0]
    # python_path = os.path.join(BIN_DIR, "python", "bin", f"python{version}")
    python_path = "python3"
    run_command([python_path, "-m", "pip", "install", "-U", "pipenv", "--user"])
    curl(tempdir, PHARMCAT_PREPROCESSOR_URL)
    unpack_tar(
        file=os.path.join(tempdir, os.path.basename(PHARMCAT_PREPROCESSOR_URL)),
        dir_=BIN_DIR,
    )
    run_command(
        f"cd {os.path.join(BIN_DIR, 'preprocessor')} && {python_path} -m pipenv install -r requirements.txt",
        shell=True,
    )


def set_env_vars():
    bash_profile = os.path.join(os.path.expanduser("~"), ".bash_profile")
    bash_profile_temp = os.path.join(os.path.expanduser("~"), ".bash_profile_temp")
    with open(bash_profile) as f_in:
        with open(bash_profile_temp, "w") as f_out:
            for line in f_in:
                if "JAVA_HOME" not in line:
                    f_out.write(line)
            for file in os.listdir(BIN_DIR):
                if "jdk" in file:
                    f_out.write(f'export JAVA_HOME="{os.path.join(BIN_DIR, file)}"\n')
    shutil.copy2(bash_profile_temp, bash_profile)
    os.remove(bash_profile_temp)


def validate_python_version(tempdir):
    if not check_python_verison():
        try:
            logger.info(
                "Incorrect version of Python was found. Attempting to install Python..."
            )
            install_python(tempdir)
        except Exception:
            try:
                shutil.rmtree(os.path.join(BIN_DIR, "python"))
            except FileNotFoundError:
                pass
            finally:
                msg = f"Requires Python v3.9+, found v{sys.version.split()[0]}. Attempt to install new version of Python was unsuccesful"
                logger.error(msg)
                raise RuntimeError(msg)
        else:
            logger.info("Successfully installed Python.")


def install(overwrite=False):
    try:
        os.mkdir(BIN_DIR)
    except FileExistsError:
        if overwrite:
            logger.info("Removing old version of PharmCAT")
            shutil.rmtree(BIN_DIR)
            logger.info("Succesfully removed old version of PharmCAT")
            os.mkdir(BIN_DIR)
        else:
            msg = "Previous installation of PharmCAT found. To install a new version, must supply --overwrite"
            logger.error(msg)
            raise FileExistsError(msg)
    try:
        with TemporaryDirectory() as tempdir:
            logger.info("***Installing PharmCAT and all required dependencies***")

            logger.info("Installing java...")
            install_java(tempdir)
            logger.info("Successfully installed java.")

            validate_python_version(tempdir)

            logger.info("Installing Preprocessor and PharmCAT pipeline...")
            install_preprocessor(tempdir)
            logger.info("Successfully installed preprocessor and PharmCAT pipeline.")

            logger.info("Downloading reference genome...")
            download_reference_genome(tempdir)
            logger.info("Succesfully downloaded reference genome.")

            logger.info("Installing PharmCAT...")
            install_pharmcat()
            logger.info("Succesfully installed PharmCAT.")

            set_env_vars()
            logger.info("Succesfully set environment variables.")
            logger.info("***Installation completed succesfully.***")
            logger.info(
                "It is recommended to restart the environment/terminal for installation to finalize."
            )
    except Exception:
        logger.exception("Installation failed")
