from monterey.tools.text import Text
from datetime import datetime
import logging
import os
from typing import Optional

class Logger:
    """
    A custom logger class for logging messages with different severity levels.

    Attributes:
        logger: A logging.Logger instance for logging messages.
        log_dir: The directory where log files will be stored.
        text: A RichText instance for styled output.
        verbose: A boolean indicating whether to display verbose output.
    """

    def __init__(self, name : str = "logger", log_dir : str ="logs", verbose : bool = False):
        """
        Initialize the Logger instance.

        Args:
            name (str): The name of the logger.
            log_dir (str, optional): The directory where log files will be stored. Defaults to "logs".
            verbose (bool, optional): Whether to display verbose output. Defaults to False.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

        log_file = f"{self.log_dir}/{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.text = Text()
        self.verbose = verbose

    def get_datetime(self):
        """
        Get the current date and time.

        Returns:
            str: The current date and time.
        """
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time = str(f"[{time}]")
        return time

    def debug(self, message : str = None, module : Optional[str] = None):
        """
        Log a debug message.

        Args:
            message (str): The message to be logged.
        """
        time = self.get_datetime()
        if self.verbose:
            if module is not None:
                self.text.display(f"[bold purple]{self.logger.name}[/bold purple] - [not bold purple]{module}[/not bold purple] | [not bold grey]{time}[not bold grey] [bold blue]DEBUG[/bold blue] - [not bold gray]{message}[/not bold gray]")
            else:
                self.text.display(f" [bold purple]{self.logger.name}[/bold purple] | [not bold grey]{time}[not bold grey] [bold blue]DEBUG[/bold blue] - [not bold gray]{message}[/not bold gray]")
        else:
            self.logger.debug(message)

    def info(self, message : str = None, module : Optional[str] = None):
        """
        Log an status message.

        Args:        message (str): The message to be logged.
        """
        time = self.get_datetime()
        if self.verbose:
            if module:
                self.text.display(f"[bold purple]{self.logger.name}[/bold purple] - [not bold purple]{module}[/not bold purple] | [not bold grey]{time}[not bold grey] [bold green]INFO[/bold green] - [not bold gray]{message}[/not bold gray]")
            else:
                self.text.display(f"[bold purple]{self.logger.name}[/bold purple] | [not bold grey]{time}[not bold grey] [bold green]INFO[/bold green] - [not bold gray]{message}[/not bold gray]")
        else:
            self.logger.info(message)

    def warning(self, message : str = None, module : Optional[str] = None):
        """
        Log a warning message.

        Args:
            message (str): The message to be logged.
        """
        time = self.get_datetime()
        if self.verbose:
            if module:
                self.text.display(f"[bold purple]{self.logger.name}[/bold purple] - [not bold purple]{module}[/not bold purple] | [not bold grey]{time}[not bold grey] [bold yellow]WARNING[/bold yellow] - [not bold gray]{message}[/not bold gray]")
            else:
                self.text.display(f"[bold purple]{self.logger.name}[/bold purple] | [not bold grey]{time}[not bold grey] [bold yellow]WARNING[/bold yellow] - [not bold gray]{message}[/not bold gray]")
        else:
            self.logger.warning(message)

    def error(self, message : str = None, module : Optional[str] = None):
        """
        Log an error message.

        Args:
            message (str): The message to be logged.
        """
        time = self.get_datetime()
        if self.verbose:
            if module:
                self.text.display(f"[bold purple]{self.logger.name}[/bold purple] - [not bold purple]{module}[/not bold purple] | [not bold grey]{time}[not bold grey] [bold red]ERROR[/bold red] - [not bold gray]{message}[/not bold gray]")
            else:
                self.text.display(f"[bold purple]{self.logger.name}[/bold purple] | [not bold grey]{time}[not bold grey] [bold red]ERROR[/bold red] - [not bold gray]{message}[/not bold gray]")
        else:
            self.logger.error(message)

    def critical(self, message : str = None, module : Optional[str] = None):
        """
        Log a critical message.

        Args:
            message (str): The message to be logged.
        """
        time = self.get_datetime()
        if self.verbose:
            if module:
                self.text.display(f"[bold purple]{self.logger.name}[/bold purple] - [not bold purple]{module}[/not bold purple] | [not bold grey]{time}[not bold grey] [bold dark_red]CRITICAL[/bold dark_red] - [not bold gray]{message}[/not bold gray]")
            else:
                self.text.display(f"[bold purple]{self.logger.name}[/bold purple] | [not bold grey]{time}[not bold grey] [bold dark_red]CRITICAL[/bold dark_red] - [not bold gray]{message}[/not bold gray]")
        else:
            self.logger.critical(message)

if __name__ == "__main__":
    logger = Logger("test", verbose=True)
    logger.debug("This is a debug message.")
    logger.info("This is an info message.", module="test")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.", module="test")
    logger.critical("This is a critical message.")
    pass