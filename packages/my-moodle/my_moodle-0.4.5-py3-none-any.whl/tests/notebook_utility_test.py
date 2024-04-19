"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Test cases for the project.
"""

from os import linesep
import unittest
from my_moodle import NotebookUtility


class TestVersion(unittest.TestCase):
    """Test case for version"""

    def test_create_jupyter_notebook_header(self) -> None:
        """Test create_jupyter_notebook_header"""
        self.maxDiff = None  # pylint: disable=invalid-name
        actual: str = NotebookUtility.create_jupyter_notebook_header(
            "marcocrowe",
            "data-analytics-project-template",
            "notebooks/notebook-2-01-example-better-code-population-eda.ipynb",
        )
        expected: str = (
            f"""<!--{linesep}import data_analytics.github as github{linesep}print(github.create_jupyter_notebook_header("marcocrowe", "data-analytics-project-template", "notebooks/notebook-2-01-example-better-code-population-eda.ipynb", "master")){linesep}-->{linesep}<table style="margin: auto;"><tr><td><a href="https://mybinder.org/v2/gh/marcocrowe/data-analytics-project-template/master?filepath=notebooks/notebook-2-01-example-better-code-population-eda.ipynb" target="_parent"><img src="https://mybinder.org/badge_logo.svg" alt="Open In Binder"/></a></td><td>online editors</td><td><a href="https://colab.research.google.com/github/marcocrowe/data-analytics-project-template/blob/master/notebooks/notebook-2-01-example-better-code-population-eda.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td></tr></table>""" # pylint: disable=line-too-long
        )
        self.assertEqual(actual.strip(), expected.strip())


if __name__ == "__main__":
    unittest.main()
