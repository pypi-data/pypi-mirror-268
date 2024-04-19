import os
import sys
from typing import Optional, Union, List, Dict, Tuple, Any
import customtkinter
from PIL import Image

class Frontend:
    """
    A lightweight and easy-to-use inline user interface module for creating simple GUIs with CustomTkinter.

    Example usage:
        ```python
        from yosemite.tools.frontend import Frontend

        ui = Frontend()
        ui.create("My App", "600x400")
        ui.set_grid_layout(3, 2)
        name_var = ui.add_textbox("Enter your name", row=1, column=1)
        ui.add_button("Click Me", command=button_click, args=[name_var], row=1, column=0)
        ui.start()

        def button_click(name):
            print(f"Button clicked! Name: {name.get()}")
        ```

    Methods:
        - create(title: str, geometry: str): Create the main application window.
        - set_grid_layout(rows: int, columns: int): Set the grid layout for the main window.
        - add_label(text: str, row: int, column: int, **kwargs): Add a label widget to the specified grid cell.
        - add_button(text: str, command: Optional[callable], args: List[Any], row: int, column: int, **kwargs): Add a button widget to the specified grid cell.
        - add_textbox(placeholder: str, row: int, column: int, **kwargs): Add a textbox widget to the specified grid cell and return the StringVar associated with it.
        - add_checkbox(text: str, command: Optional[callable], args: List[Any], row: int, column: int, **kwargs): Add a checkbox widget to the specified grid cell and return the BooleanVar associated with it.
        - add_radio_button(text: str, value: str, row: int, column: int, **kwargs): Add a radio button widget to the specified grid cell.
        - add_slider(from_: float, to: float, command: Optional[callable], args: List[Any], row: int, column: int, **kwargs): Add a slider widget to the specified grid cell and return the DoubleVar associated with it.
        - add_option_menu(values: List[str], command: Optional[callable], args: List[Any], row: int, column: int, **kwargs): Add an option menu widget to the specified grid cell and return the StringVar associated with it.
        - add_image(path: str, size: Tuple[int, int], row: int, column: int, **kwargs): Add an image widget to the specified grid cell.
        - set_font(font_family: str, size: int): Set the default font for all widgets.
        - start(): Start the main event loop of the application.
    """

    def __init__(self):
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        self.app = customtkinter.CTk()
        self.font = customtkinter.CTkFont(family="Arial", size=12)
        self.radio_var = None

    def create(self, title: str = "InlineUI App", geometry: str = "600x400"):
        """
        Create the main application window.

        Args:
            title (str): The title of the window. Default is "InlineUI App".
            geometry (str): The geometry of the window in the format "widthxheight". Default is "600x400".
        """
        self.app.title(title)
        self.app.geometry(geometry)

    def set_grid_layout(self, rows: int = 1, columns: int = 1):
        """
        Set the grid layout for the main window.

        Args:
            rows (int): The number of rows in the grid. Default is 1.
            columns (int): The number of columns in the grid. Default is 1.
        """
        for i in range(rows):
            self.app.grid_rowconfigure(i, weight=1)
        for i in range(columns):
            self.app.grid_columnconfigure(i, weight=1)

    def add_label(self, text: str = "", row: int = 0, column: int = 0, **kwargs):
        """
        Add a label widget to the specified grid cell.

        Args:
            text (str): The text to display in the label. Default is an empty string.
            row (int): The row index of the grid cell. Default is 0.
            column (int): The column index of the grid cell. Default is 0.
            **kwargs: Additional keyword arguments to pass to the CTkLabel constructor.
        """
        label = customtkinter.CTkLabel(self.app, text=text, font=self.font, **kwargs)
        label.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

    def add_button(self, text: str = "Button", command: Optional[callable] = None, args: List[Any] = None, row: int = 0, column: int = 0, **kwargs):
        """
        Add a button widget to the specified grid cell.

        Args:
            text (str): The text to display on the button. Default is "Button".
            command (Optional[callable]): The function to be called when the button is clicked. Default is None.
            args (List[Any]): The arguments to pass to the command function. Default is None.
            row (int): The row index of the grid cell. Default is 0.
            column (int): The column index of the grid cell. Default is 0.
            **kwargs: Additional keyword arguments to pass to the CTkButton constructor.
        """
        if args is None:
            args = []
        button = customtkinter.CTkButton(self.app, text=text, command=lambda: command(*args), font=self.font, **kwargs)
        button.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

    def add_textbox(self, placeholder: str = "Enter text", row: int = 0, column: int = 0, **kwargs):
        """
        Add a textbox widget to the specified grid cell.

        Args:
            placeholder (str): The placeholder text for the textbox. Default is "Enter text".
            row (int): The row index of the grid cell. Default is 0.
            column (int): The column index of the grid cell. Default is 0.
            **kwargs: Additional keyword arguments to pass to the CTkEntry constructor.

        Returns:
            customtkinter.StringVar: The StringVar associated with the textbox.
        """
        textvar = customtkinter.StringVar()
        textbox = customtkinter.CTkEntry(self.app, placeholder_text=placeholder, textvariable=textvar, font=self.font, **kwargs)
        textbox.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")
        return textvar

    def add_checkbox(self, text: str = "Checkbox", command: Optional[callable] = None, row: int = 0, column: int = 0, **kwargs):
        """
        Add a checkbox widget to the specified grid cell.

        Args:
            text (str): The text to display next to the checkbox. Default is "Checkbox".
            command (Optional[callable]): The function to be called when the checkbox is clicked. Default is None.
            row (int): The row index of the grid cell. Default is 0.
            column (int): The column index of the grid cell. Default is 0.
            **kwargs: Additional keyword arguments to pass to the CTkCheckBox constructor.

        Returns:
            customtkinter.BooleanVar: The BooleanVar associated with the checkbox.
        """
        checkvar = customtkinter.BooleanVar()
        checkbox = customtkinter.CTkCheckBox(self.app, text=text, variable=checkvar, command=lambda: command(checkvar) if command else None, font=self.font, **kwargs)
        checkbox.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")
        return checkvar

    def add_radio_button(self, text: str = "Radio Button", value: str = "", row: int = 0, column: int = 0, **kwargs):
        """
        Add a radio button widget to the specified grid cell.

        Args:
            text (str): The text to display next to the radio button. Default is "Radio Button".
            value (str): The value to assign to the radio button. Default is an empty string.
            row (int): The row index of the grid cell. Default is 0.
            column (int): The column index of the grid cell. Default is 0.
            **kwargs: Additional keyword arguments to pass to the CTkRadioButton constructor.
        """
        if self.radio_var is None:
            self.radio_var = customtkinter.StringVar(value=value)
        radio_button = customtkinter.CTkRadioButton(self.app, text=text, variable=self.radio_var, value=value, font=self.font, **kwargs)
        radio_button.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

    def add_slider(self, from_: float = 0, to: float = 100, command: Optional[callable] = None, args: List[Any] = None, row: int = 0, column: int = 0, **kwargs):
        """
        Add a slider widget to the specified grid cell.

        Args:
            from_ (float): The minimum value of the slider. Default is 0.
            to (float): The maximum value of the slider. Default is 100.
            command (Optional[callable]): The function to be called when the slider value changes. Default is None.
            args (List[Any]): The arguments to pass to the command function. Default is None.
            row (int): The row index of the grid cell. Default is 0.
            column (int): The column index of the grid cell. Default is 0.
            **kwargs: Additional keyword arguments to pass to the CTkSlider constructor.

        Returns:
            customtkinter.DoubleVar: The DoubleVar associated with the slider.
        """
        if args is None:
            args = []
        slidervar = customtkinter.DoubleVar()
        slider = customtkinter.CTkSlider(self.app, from_=from_, to=to, variable=slidervar, command=lambda value: command(value, *args), **kwargs)
        slider.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")
        return slidervar

    def add_option_menu(self, values: List[str] = ["Option 1", "Option 2"], command: Optional[callable] = None, args: List[Any] = None, row: int = 0, column: int = 0, **kwargs):
        """
        Add an option menu widget to the specified grid cell.

        Args:
            values (List[str]): The list of options to display in the menu. Default is ["Option 1", "Option 2"].
            command (Optional[callable]): The function to be called when an option is selected. Default is None.
            args (List[Any]): The arguments to pass to the command function. Default is None.
            row (int): The row index of the grid cell. Default is 0.
            column (int): The column index of the grid cell. Default is 0.
            **kwargs: Additional keyword arguments to pass to the CTkOptionMenu constructor.

        Returns:
            customtkinter.StringVar: The StringVar associated with the option menu.
        """
        if args is None:
            args = []
        optionvar = customtkinter.StringVar(value=values[0])
        option_menu = customtkinter.CTkOptionMenu(self.app, values=values, variable=optionvar, command=lambda choice: command(choice, *args), font=self.font, **kwargs)
        option_menu.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")
        return optionvar

    def add_image(self, path: str, size: Tuple[int, int] = (200, 200), row: int = 0, column: int = 0, **kwargs):
        """
        Add an image widget to the specified grid cell.

        Args:
            path (str): The path to the image file.
            size (Tuple[int, int]): The size of the image in the format (width, height). Default is (200, 200).
            row (int): The row index of the grid cell. Default is 0.
            column (int): The column index of the grid cell. Default is 0.
            **kwargs: Additional keyword arguments to pass to the CTkLabel constructor.
        """
        image = customtkinter.CTkImage(Image.open(path), size=size)
        image_label = customtkinter.CTkLabel(self.app, image=image, text="", **kwargs)
        image_label.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

    def set_font(self, font_family: str = "Arial", size: int = 12):
        """
        Set the default font for all widgets.

        Args:
            font_family (str): The font family name. Default is "Arial".
            size (int): The font size. Default is 12.
        """
        self.font = customtkinter.CTkFont(family=font_family, size=size)

    def start(self):
        """
        Start the main event loop of the application.
        """
        self.app.mainloop()


if __name__ == "__main__":
    ui = Frontend()
    ui.create("My App", "600x400")
    ui.set_grid_layout(5, 2)
    ui.set_font("Helvetica", 14)

    name_var = ui.add_textbox("Enter your name", row=1, column=1)

    def button_click(name):
        print(f"Button clicked! Name: {name.get()}")

    ui.add_label("Welcome to My App", row=0, column=0)
    ui.add_button("Click Me", command=button_click, args=[name_var], row=1, column=0)

    def checkbox_click(checkvar):
        print(f"Checkbox clicked! Value: {checkvar.get()}")

    check_var = ui.add_checkbox("I agree to the terms and conditions", command=checkbox_click, row=2, column=0)

    ui.add_radio_button("Option 1", value="option1", row=2, column=1)
    ui.add_radio_button("Option 2", value="option2", row=3, column=1)

    def slider_changed(value):
        print(f"Slider value changed: {value}")

    slider_var = ui.add_slider(0, 100, command=slider_changed, row=3, column=0)

    def option_selected(choice):
        print(f"Option selected: {choice}")

    option_var = ui.add_option_menu(["Option 1", "Option 2", "Option 3"], command=option_selected, row=4, column=0)

    ui.start()