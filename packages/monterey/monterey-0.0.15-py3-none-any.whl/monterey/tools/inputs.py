from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from getpass import getpass

class Input:
    def __init__(self):
        """
        A lightweight class for handling user inputs in the terminal.
        Uses Prompt Toolkit for both simple CLI text and expressive GUI dialogs.

        Attributes:
        pause: A method to pause the terminal until the user presses Enter.
        confirm: A method to prompt the user for a yes/no confirmation.
        ask: A method to prompt the user for input in the terminal.
        hide: A method to prompt the user for input in the terminal, hiding the input (for passwords).
        choice: A method to prompt the user to select from a list of choices.
        """
        pass

    @staticmethod
    def pause(message: str = None):
        """
        Pauses the terminal until the user presses Enter.

        Example:
        ```python
        from yosemite.tools.input import Input
        Input.pause()
        ```

        Args:
        message (str): The message to display to the user.
        """
        if not message:
            message = "Press Enter to continue..."
        input(message)

    @staticmethod
    def confirm(message: str = None):
        """
        Prompt the user for a yes/no confirmation.

        Example:
        ```python
        Input.confirm("Are you sure?")
        ```

        Args:
        message (str): The message to display to the user.
        """
        if not message:
            message = "Are you sure? (y/n): "
        else:
            message = f"{message} (y/n): "
        while True:
            value = input(message).lower()
            if value in ('y', 'yes'):
                return True
            elif value in ('n', 'no'):
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    @staticmethod
    def ask(message: str = None):
        """
        Prompt the user for input in the terminal.

        Example:
        ```python
        name = Input.ask("What is your name?")
        print(f"Hello, {name}!")
        ```

        ```bash
        Hello, John!
        ```

        Args:
        message (str): The message to display to the user.
        """
        if not message:
            message = ""
        if message:
            message = f"{message} "
        if message:
            value = prompt(message)
            return value
        else:
            print("'message' is required for prompt_input()")

    @staticmethod
    def hide(message: str = None):
        """
        Prompt the user for input in the terminal, hiding the input (for passwords).

        Example:
        ```python
        password = Input.hide("Enter your password:")
        print("Password entered successfully!")
        ```

        Args:
        message (str): The message to display to the user.
        """
        if not message:
            message = ""
        if message:
            message = f"{message} "
        if message:
            value = getpass(message)
            return value
        else:
            print("'message' is required for prompt_password()")

    @staticmethod
    def choice(message: str = None, choices: list = None):
        """
        Prompt the user to select from a list of choices.

        Example:
        ```python
        list = ["Red", "Green", "Blue"]
        color = Input.choice("Choose a color:", list)
        print(f"You chose {color}.")
        ```

        ```bash
        You chose Red.
        ```

        Args:
        message (str): The message to display to the user.
        choices (list): A list of choices for the user to select from.
        """
        if not message:
            message = ""
        if message:
            message = f"{message} "
        if message and choices:
            value = prompt(message=message, completer=WordCompleter(words=choices))
            return value
        else:
            print("'message' and 'choices' are required for prompt_choice()")

#==============================================================================#
if __name__ == "__main__":
    list = ["Red", "Green", "Blue"]
    Input.pause()
    Input.ask("What is your name?")
    Input.confirm("Are you sure?")
    Input.hide("Enter your password:")
    Input.choice("Choose a color:", list)