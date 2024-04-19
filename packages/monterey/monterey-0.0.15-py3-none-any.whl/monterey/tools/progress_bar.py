from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.panel import Panel
from rich import box

# ==============================================================================

class ProgressBar:
    """Displays a progress bar using the Rich library.

    Attributes:
        total (int): The total number of steps in the progress.
        use_box (bool): Whether to wrap the progress bar in a use_box.
    """

    def __init__(self, total: int, use_box: bool = False):
        """
        Initializes the RichProgress with the total number of steps and use_box option.

        Example:
            ```python
            from yosemite.tools.load import RichProgress

            progress = RichProgress(total=100, use_box=True)
            with progress:
                for i in range(100):
                    progress.update(i)
                    time.sleep(0.1)
            ```

        Args:
            total (int): The total number of steps in the progress.
            use_box (bool, optional): Whether to wrap the progress bar in a use_box. Defaults to False.
        """
        self.console = Console()
        self.total = total
        self.use_box = use_box

    def __enter__(self):
        self.progress = Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
            console=self.console,
        )
        self.task = self.progress.add_task("[cyan]Processing...", total=self.total)
        if self.use_box:
            self.progress = Panel(self.progress, expand=False, box=box.ROUNDED)
        self.progress.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.progress.stop()

    def update(self, completed: int):
        """Updates the progress bar with the number of completed steps.

        Args:
            completed (int): The number of completed steps.
        """
        self.progress.update(self.task, completed=completed)

# ==============================================================================

if __name__ == "__main__":
    import time
    
    progress = ProgressBar(total=100, use_box=True)
    with progress:
        for i in range(100):
            progress.update(i)
            time.sleep(0.1)