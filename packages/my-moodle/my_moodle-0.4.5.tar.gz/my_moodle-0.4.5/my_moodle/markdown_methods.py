"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Markdown Methods
"""


class MarkdownLink:
    """A class for creating markdown links."""

    def __init__(self, text: str, location: str, title: str = ""):
        """Create a markdown link

        Args:
            text (str): The text to display
            location (str): The location target
            title (str, optional): The title of the link. Defaults to None.
        """
        self.text = text
        """The text to display"""
        self.location = location
        """The location target"""
        self.title = title
        """The title of the link. Defaults to None."""

    def __str__(self) -> str:
        """Converts the link to a markdown string

        Returns:
            str: The markdown link string
        """
        if self.title and self.title != "":
            title = self.title.replace('"', "'")
            return f'[{self.text}]({self.location} "{title}")'
        return f"[{self.text}]({self.location})"


class MarkdownImage:
    """A class for creating markdown images."""

    def __init__(self, alt_text: str, location: str, title: str = ""):
        """Create a markdown image

        Args:
            alt_text (str): The alt text for the image
            location (str): The location of the image
            title (str): The title of the image
        """
        self.alt_text = alt_text
        """The alt text for the image"""
        self.location = location
        """The location of the image"""
        self.title = title
        """The title of the image"""

    def __str__(self) -> str:
        """Converts the image to a markdown string

        Returns:
            str: The markdown image string
        """
        if self.title:
            return f'![{self.alt_text}]({self.location} "{self.title}")'
        return f"![{self.alt_text}]({self.location})"

def bullet(text: str, level: int = 0, intent_text: str = "  ") -> str:
    """Turns raw text into a markdown bullet

    Args:
        text (str): The text to display

    Returns:
        str: The markdown bullet
    """
    return f"{level * intent_text}- {text}"


def heading(text: str, level: int = 1) -> str:
    """Create a markdown heading

    Args:
        text (str): The text to display
        level (int, optional): The level of the heading. Defaults to 1.

    Returns:
        str: The markdown heading
    """
    return f"{level * '#'} {text}"


def hr() -> str:
    """Create a markdown horizontal rule

    Returns:
        str: The markdown horizontal rule
    """
    return "---\n"


def image(alt_text: str, location: str, title: str = "") -> str:
    """Creates a markdown image

    Args:
        alt_text (str): The alt text for the image
        location (str): The location of the image
        title (str): The title of the image

    Returns:
        str: The markdown image
    """
    if title:
        return f'![{alt_text}]({location} "{title}")'
    else:
        return f"![{alt_text}]({location})"


def link(text: str, location: str, title: str = "") -> str:
    """Creates a markdown link

    Args:
        text (str): The text to display
        location (str): The location target
        title (str, optional): The title of the link. Defaults to None. Defaults to None.

    Returns:
        str: The markdown link
    """
    return f'[{text}]({location} "{title}")' if title else f"[{text}]({location})"
