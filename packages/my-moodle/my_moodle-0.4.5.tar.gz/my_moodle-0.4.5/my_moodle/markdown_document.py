"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Markdown Document Class
"""

from io import StringIO
from .markdown_methods import MarkdownImage, MarkdownLink, bullet, hr


class MarkdownDocument:
    """A class for creating markdown documents."""

    def __init__(self, indentation: str = ""):
        self._contents: StringIO = StringIO()
        """Container for the text of the markdown document"""
        self.indentation = indentation if indentation else "  "
        """A string prefix used to indent text. i.e. tabs or spaces. 
        Defaults to two spaces ('  ')"""

    def write(self, text: str) -> "MarkdownDocument":
        """Writes text to the markdown document

        Args:
            text (str): The text to append

        Returns:
            MarkdownDocument: The markdown document
        """
        self._contents.write(text)
        return self

    def write_indented(self, text: str, level: int) -> "MarkdownDocument":
        """Writes text to the markdown document with indentation

        Args:
            text (str): The text to append
            level (int): The level of the indentation

        Returns:
            MarkdownDocument: The markdown document
        """
        return self.write(f"{level * self.indentation} {text}")

    def write_indented_line(self, text: str, level: int) -> "MarkdownDocument":
        """Writes text to the markdown document with indentation and appends a newline character

        Args:
            text (str): The text to append
            level (int): The level of the indentation

        Returns:
            MarkdownDocument: The markdown document
        """
        return self.write(f"{level * self.indentation} {text}")

    def write_line(self, text: str = "") -> "MarkdownDocument":
        """Writes text to the markdown document and appends a newline character

        Args:
            text (str): The text to append

        Returns:
            MarkdownDocument: The markdown document
        """
        return self.write(f"{text}\n") if text else self.write("\n")

    def write_paragraph(self, text: str) -> "MarkdownDocument":
        """Writes text to the markdown document and appends 2 newline characters

        Args:
            text (str): The text to append as a paragraph

        Returns:
            MarkdownDocument: The markdown document
        """
        return self.write(f"{text}\n\n") if text else self

    def write_link(self, link: MarkdownLink, level: int = 0) -> "MarkdownDocument":
        """Writes a link to the markdown document

        Args:
            link (MarkdownLink): The link to append
            level (int, optional): The level of the indentation. Defaults to 0.

        Returns:
            MarkdownDocument: The markdown document
        """
        return self.write_indented(str(link), level)

    def write_bullet_link_line(
        self, link: MarkdownLink, level: int = 0
    ) -> "MarkdownDocument":
        """Writes a bulleted link to the markdown document

        Args:
            link (MarkdownLink): The link to append
            level (int, optional): The level of the indentation. Defaults to 0.

        Returns:
            MarkdownDocument: The markdown document
        """
        return self.write_bullet_line(str(link), level)

    def write_bullet_line(self, text: str, level=0) -> "MarkdownDocument":
        """Writes a bulleted line to the markdown document

        Args:
            text (str): _description_
            level (int, optional): _description_. Defaults to 0.

        Returns:
            MarkdownDocument: The markdown document
        """
        return self.write_line(bullet(text, level))

    def close(self) -> "MarkdownDocument":
        """Closes the markdown document
        This method should be called when the document is no longer being modified.

        Returns:
            MarkdownDocument: _description_
        """
        self._contents.close()
        return self

    def __str__(self) -> str:
        """Returns the contents of the markdown document

        Returns:
            str: The contents of the markdown document
        """
        return self._contents.getvalue()

    def write_h1(self, text: str) -> "MarkdownDocument":
        """Writes an h1 to the markdown document

        Args:
            text (str): The text of the h1

        Returns:
            MarkdownDocument: The markdown document
        """
        return self.write_line(f"# {text}\n")

    def write_h2(self, text: str) -> "MarkdownDocument":
        """Writes an h2 to the markdown document

        Args:
            text (str): The text of the h2

        Returns:
            MarkdownDocument: The markdown document
        """
        return self.write_line(f"## {text}\n")

    def write_h3(self, text: str) -> "MarkdownDocument":
        """Writes an h3 to the markdown document

        Args:
            text (str): The text of the h3

        Returns:
            MarkdownDocument: The markdown document
        """
        return self.write_line(f"### {text}\n")

    def write_h4(self, text: str) -> "MarkdownDocument":
        """Writes an h4 to the markdown document

        Args:
            text (str): The text of the h4

        Returns:
            MarkdownDocument: The markdown document
        """
        return self.write_line(f"#### {text}\n")

    def write_heading(self, text: str, level=1) -> "MarkdownDocument":
        """Writes a heading to the markdown document

        Args:
            text (str): The text of the heading
            level (int, optional): The level of the heading. Defaults to 1.

        Returns:
            MarkdownDocument: The markdown document
        """
        return self.write_line(f"{level * '#'} {text}\n")

    def write_hr(self) -> "MarkdownDocument":
        """Writes a horizontal rule to the markdown document

        Returns:
            MarkdownDocument: The markdown document
        """
        return self.write(hr())

    def write_image(self, image: MarkdownImage) -> "MarkdownDocument":
        """Writes an image to the markdown document

        Args:
            image (MarkdownImage): The image to append

        Returns:
            MarkdownDocument: The markdown document
        """
        return self.write(str(image))

    def save_to_file(self, file_path: str, encoding: str) -> None:
        """Saves the markdown document to a file

        Args:
            file_path (str): The file path
        """
        with open(file_path, "w", encoding=encoding) as file:
            file.write(str(self))
