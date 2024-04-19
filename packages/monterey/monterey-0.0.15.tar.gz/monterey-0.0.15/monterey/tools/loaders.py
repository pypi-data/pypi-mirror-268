from rich.console import Console
from rich.status import Status
from rich.panel import Panel
from rich import box

# ==============================================================================

class Loader:
    """Displays an animated loading status using the Rich library.

    Attributes:
        message (str): The message to be displayed while loading.
        spinner (str): The spinner style to be used for the loading animation.
        use_box (bool): Whether to wrap the loading message in a use_box.
    """

    def __init__(self, message: str = "Loading...", spinner: str = "dots", use_box: bool = False):
        """
        Initializes the RichLoader with a message, spinner style, and use_box option.

        Example:
            ```python
            from yosemite.tools.loaders import Loader

            loader = RichLoader(message="Processing data", spinner="dots", use_box=True)
            with loader:
                time.sleep(2)
                loader.update("Processing step 1")
                time.sleep(2)
                loader.update("Processing step 2")
                time.sleep(2)
            ```

        Args:
            message (str, optional): The message to be displayed while loading. Defaults to "Loading...".
            spinner (str, optional): The spinner style to be used for the loading animation. Defaults to "dots".
            use_box (bool, optional): Whether to wrap the loading message in a use_box. Defaults to False.
        """
        self.console = Console()
        self.message = message
        self.spinner = spinner
        self.use_box = use_box

    def __enter__(self):
        if self.use_box:
            self.status = Status(Panel(self.message, expand=False, box=box.ROUNDED), spinner=self.spinner)
        else:
            self.status = Status(self.message, spinner=self.spinner)
        self.status.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.status.stop()

    def update(self, message: str):
        """Updates the loading message while the loader is running.

        Example:
            ```python
            loader = Loader()
            with loader:
                time.sleep(2)
                loader.update("Processing step 1")
                time.sleep(2)
                loader.update("Processing step 2")
                time.sleep(2)
            ```

        Args:
            message (str): The updated message to be displayed.
        """
        self.status.update(Panel(message, expand=False, box=box.ROUNDED) if self.use_box else message)

# ==============================================================================

if __name__ == "__main__":
    import time
    
    loader = Loader(message="Processing data", spinner="dots", use_box=True)
    with loader:
        time.sleep(2)
        loader.update("Processing step 1")
        time.sleep(2)
        loader.update("Processing step 2")
        time.sleep(2)