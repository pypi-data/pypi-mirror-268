from IPython.display import display, HTML
from typing import Optional, List, Union, Tuple

class Tailwind:
    """
    A class for creating and displaying HTML elements with Tailwind CSS, Material-UI styles, and custom fonts in Jupyter notebooks.
    """

    def __init__(self, className : Optional[str] = None):
        self.className = className
        if self.className is not None:
            self.html_template = """
            <!DOCTYPE html>
            <html>
            <head>
                <script src="https://cdn.tailwindcss.com"></script>
                <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Lexend:wght@400;500;600;700&family=Lora:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
                <style>
                    body {{ font-family: 'DM Sans', sans-serif; }}
                    h1, h2, h3, h4, h5, h6 {{ font-family: 'Lexend', sans-serif; }}
                    p {{ font-family: 'Lora', serif; }}
                    code, pre {{ font-family: 'JetBrains Mono', monospace; }}
                    .playfair {{ font-family: 'Playfair Display', serif; }}
                    .dm-sans {{ font-family: 'DM Sans', sans-serif; }}
                    .lexend {{ font-family: 'Lexend', sans-serif; }}
                    .lora {{ font-family: 'Lora', serif; }}
                    .jetbrains-mono {{ font-family: 'JetBrains Mono', monospace; }}
                </style>
            </head>
            <body>
                <div class='{className}'>
                {content}
                </div>
            </body>
            </html>
            """
        else:
            self.html_template = """
            <!DOCTYPE html>
            <html>
            <head>
                <script src="https://cdn.tailwindcss.com"></script>
                <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Lexend:wght@400;500;600;700&family=Lora:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
                <style>
                    body {{ font-family: 'DM Sans', sans-serif; }}
                    h1, h2, h3, h4, h5, h6 {{ font-family: 'Lexend', sans-serif; }}
                    p {{ font-family: 'Lora', serif; }}
                    code, pre {{ font-family: 'JetBrains Mono', monospace; }}
                    .dm-sans {{ font-family: 'DM Sans', sans-serif; }}
                    .lexend {{ font-family: 'Lexend', sans-serif; }}
                    .lora {{ font-family: 'Lora', serif; }}
                    .jetbrains-mono {{ font-family: 'JetBrains Mono', monospace; }}
                    .playfair {{ font-family: 'Playfair Display', serif; }}
                </style>
            </head>
            <body>
                {content}
            </body>
            </html>
            """

    def display(self, content: str, className: Optional[str] = "", component: Optional[str] = "div"):
        """
        Display the HTML element with the specified content, component type, and Tailwind CSS class.

        Args:
            content (str): The content of the HTML element.
            component (str, optional): The HTML component type. Defaults to "div".
            className (str, optional): The Tailwind CSS class name. Defaults to an empty string.
        """
        element = f"<{component} class='{className}'>{content}</{component}>"
        if self.className is not None:
            html = self.html_template.format(content=element, className=self.className)
        else:
            html = self.html_template.format(content=element)
        display(HTML(html))

    def display_components(self, components: List[Union[str, Tuple[str, str]]], className: Optional[str] = ""):
        """
        Display multiple components inside a div with the specified Tailwind CSS class.
        
        Args:
            components (List[Union[str, Tuple[str, str]]]): A list of components to be displayed.
                Each component can be either a string (content) or a tuple (content, className).
            className (str, optional): The Tailwind CSS class name for the outer div. Defaults to an empty string.
        """
        elements = []
        for component in components:
            if isinstance(component, str):
                content = component
                component_className = ""
            else:
                content, component_className = component
            element = f"<div class='{component_className}'>{content}</div>"
            elements.append(element)
        
        content = "\n".join(elements)
        if self.className is not None:
            div_className = f"{self.className} {className}"
        else:
            div_className = className
        html = self.html_template.format(content=content, className=div_className)
        display(HTML(html))

# ==============================

if __name__ == "__main__":
    tailwind = Tailwind()

    components = [
        "This is a plain string component",
        ("This is a component with a className", "text-blue-500 font-bold"),
        "Another plain string component",
        ("Last component with a different className", "bg-gray-200 p-4"),
    ]

    tailwind.display_components(components, className="container mx-auto")