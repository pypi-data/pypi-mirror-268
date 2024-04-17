import logging
import shutil
import tempfile

from git import Repo


# Clone a Git repository to a temporary directory and handle errors.
def clone_remote_repo(url):
    temp_dir = tempfile.mkdtemp()  # Creates temporary directory
    try:
        Repo.clone_from(url, temp_dir)  # Clones the repo
        logging.info("Repository cloned successfully.")
        return temp_dir  # Returns path to the cloned repo
    except Exception as e:
        logging.error(f"Cloning failed: {e}")  # Logs cloning failure
        shutil.rmtree(
            temp_dir, ignore_errors=True
        )  # Removes the temporary directory on failure
        return None  # Returns None if cloning fails
