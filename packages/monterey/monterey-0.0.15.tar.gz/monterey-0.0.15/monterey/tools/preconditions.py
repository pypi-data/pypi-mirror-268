from monterey.tools.logger import Logger
import pathlib
from typing import Optional

# =============================================================================

class Preconditions:
    def __init__(self, logger: Optional[Logger] = None):
        """
        A class for verifying preconditions before executing code.

        Attributes:
            logger: A Logger instance for logging messages.
        """
        self.logger = logger

    def check_dir_exists(self, path: str) -> str:
        """
        Checks if a directory exists.

        Example:
            ```python
            from yosemite.tools.preconditions import Preconditions

            preconditions = Preconditions()
            preconditions.check_dir_exists("C:/Users/username/Desktop")
            ```

        Args:
            path (str): The path to the directory.

        Returns:
            str: The path to the directory.
        """
        if not path:
            self._log_and_raise("Path is required!", ValueError)

        try:
            path = pathlib.Path(path)
            if not path.exists():
                self._log_and_raise(f"Directory not found: {path}", FileNotFoundError)
            if not path.is_dir():
                self._log_and_raise(f"Path is not a directory: {path}", ValueError)
        except Exception as e:
            self._log_and_raise(f"Error reading path: {e}", ValueError)

        self._log_info(f"Directory exists: {path}")
        return str(path)

    def check_file_exists(self, path: str) -> str:
        """
        Checks if a file exists.

        Example:
            ```python
            from yosemite.tools.preconditions import Preconditions

            preconditions = Preconditions()
            preconditions.check_file_exists("C:/Users/username/Desktop/file.txt")
            ```

        Args:
            path (str): The path to the file.

        Returns:
            str: The path to the file.
        """
        if not path:
            self._log_and_raise("Path is required!", ValueError)

        try:
            path = pathlib.Path(path)
            if not path.exists():
                self._log_and_raise(f"File not found: {path}", FileNotFoundError)
            if not path.is_file():
                self._log_and_raise(f"Path is not a file: {path}", ValueError)
        except Exception as e:
            self._log_and_raise(f"Error reading: {e}", ValueError)

        self._log_info(f"File exists: {path}")
        return str(path)

    def create_path(self, path: str) -> str:
        """
        Creates a directory if it does not exist.

        Example:
            ```python
            from yosemite.tools.preconditions import Preconditions

            preconditions = Preconditions()
            preconditions.create_path("C:/Users/username/Desktop")
            ```

        Args:
            path (str): The path to the directory.

        Returns:
            str: The path to the directory.
        """
        try:
            path = pathlib.Path(path)
            path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            self._log_and_raise(f"Error creating path: {e}", ValueError)

        self._log_info(f"Path created: {path}")
        return str(path)

    def _log_info(self, message: str):
        if self.logger:
            self.logger.info(message, module="Precondition Verifier")

    def _log_and_raise(self, message: str, exception: Exception):
        if self.logger:
            if isinstance(exception, FileNotFoundError):
                self.logger.error(message, module="Precondition Verifier")
            elif isinstance(exception, ValueError):
                self.logger.critical(message, module="Precondition Verifier")
        raise exception(message)
    
# =============================================================================

if __name__ == "__main__":
    from monterey.tools.logger import Logger

    logger = Logger(verbose=True)
    preconditions = Preconditions()

    preconditions.check_dir_exists("C:/Users/username/Desktop")