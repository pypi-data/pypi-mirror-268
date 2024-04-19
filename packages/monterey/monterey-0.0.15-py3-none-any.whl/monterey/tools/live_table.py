from rich.console import Console
from rich.live import Live
from rich.table import Table

# ==============================================================================

class LiveTable:
    """Displays a live updating table using the Rich library."""

    def __init__(self):
        """
        Initializes the RichLiveTable.

        Example:
            ```python
            from yosemite.tools.live_table import LiveTable

            table = LiveTable()
            with table:
                for i in range(10):
                    table.add_row(f"Row {i}", str(random.randint(0, 100)))
                    time.sleep(1)
            ```
        """
        self.console = Console()
        self.table = Table(show_header=True, header_style="bold magenta")
        self.table.add_column("Item", style="dim")
        self.table.add_column("Value")

    def __enter__(self):
        self.live = Live(self.table, console=self.console)
        self.live.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.live.stop()

    def add_row(self, item: str, value: str):
        """Adds a row to the live updating table.

        Args:
            item (str): The item name.
            value (str): The item value.
        """
        self.table.add_row(item, value)

# ==============================================================================

if __name__ == "__main__":
    import random
    import time

    table = LiveTable()
    with table:
        for i in range(10):
            table.add_row(f"Row {i}", str(random.randint(0, 100)))
            time.sleep(1)