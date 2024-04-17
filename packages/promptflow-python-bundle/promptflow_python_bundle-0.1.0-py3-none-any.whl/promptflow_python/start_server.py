# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import os
import shutil
from pathlib import Path

from promptflow._utils.logger_utils import service_logger


def ensure_runit_installed():
    """Ensure runit is installed."""
    if shutil.which("runsvdir") is None:
        raise RuntimeError("'runsvdir' is required. Please install 'runit' before starting the service.")
    service_logger.info("'runit' has been installed.")


def ensure_procps_installed():
    """Ensure procps is installed."""
    if shutil.which("pgrep") is None or shutil.which("pkill") is None:
        raise RuntimeError("'pgrep' and 'pkill' is required. Please install 'procps' before starting the service.")
    service_logger.info("'procps' has been installed.")


def copy_package_data():
    # Ensure the package data folder exists
    package_data_folder = Path(__file__).resolve().parent / "package_data"
    if not package_data_folder.exists():
        raise RuntimeError(f"The package data folder {package_data_folder} of promptflow-python-bundle not found.")
    service_logger.info(f"Find promptflow-python-bundle package data: {package_data_folder}")
    # Copy some folders under package_data to the target directory
    scripts_folder = package_data_folder / "scripts"
    runit_folder = package_data_folder / "runit"
    directory_mappings = {
        scripts_folder: Path("/service/scripts"),
        runit_folder: Path("/var/runit"),
    }
    for source, destination in directory_mappings.items():
        copy_directory(source, destination)


def copy_directory(source: Path, destination: Path):
    """Copy the source directory to the destination directory and set the permission."""
    shutil.copytree(source, destination, dirs_exist_ok=True)
    for root, dirs, files in os.walk(destination):
        for d in [os.path.join(root, d) for d in dirs]:
            os.chmod(d, 0o755)
        for f in [os.path.join(root, f) for f in files]:
            os.chmod(f, 0o755)
    service_logger.info(f"Copy {source} to: {destination}.")


def main():
    try:
        service_logger.info("Starting promptflow-python app...")
        # Ensure required packages are installed
        ensure_runit_installed()
        ensure_procps_installed()
        copy_package_data()
        # Run bash script in current process
        os.execvp("bash", ["bash", "/service/scripts/start.sh"])
    except Exception as e:
        service_logger.error(f"Failed to start promptflow-python app: {e}")
        raise


if __name__ == "__main__":
    main()
