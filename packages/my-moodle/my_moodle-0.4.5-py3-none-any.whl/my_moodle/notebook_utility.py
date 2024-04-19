"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Notebook utility
"""

from os import linesep
from IPython.display import display
from IPython.core.display import HTML
from .resource_utility import PackageResources


def create_jupyter_notebook_header(
    github_username: str,
    repository: str,
    notebook_filepath: str,
    branch: str = "master",
    style: str = 'style="margin: auto;"',
) -> str:
    """Create an edit online header for Jupyter Notebook.

    Args:
        github_username (str): The GitHub username
        repository (str): The repository name
        notebook_filepath (str): The notebook filepath relative to the repository root
        branch (str, optional): The branch name. Defaults to 'master'.
        style (_type_, optional): The style attribute. Defaults to 'style="margin: auto;"'.

    Returns:
        str: The HTML header
    """

    package_resources = PackageResources()
    html_comment: str = package_resources.html_comment.format(
        linesep=linesep,
        github_username=github_username,
        repository=repository,
        notebook_filepath=notebook_filepath,
        branch=branch,
    )

    binder_url: str = package_resources.binder_url.format(
        github_username=github_username,
        repository=repository,
        branch=branch,
        notebook_filepath=notebook_filepath,
    )

    colab_url: str = package_resources.colab_url.format(
        github_username=github_username,
        repository=repository,
        branch=branch,
        notebook_filepath=notebook_filepath,
    )

    open_with_table: str = package_resources.open_with_table.format(
        style=style, binder_url=binder_url, colab_url=colab_url
    )

    return f"{html_comment}{open_with_table}"


def display_jupyter_notebook_header(
    github_username: str,
    repository: str,
    notebook_filepath: str = "notebook-main.ipynb",
    branch: str = "master",
) -> None:
    """Display an edit online header for Jupyter Notebook.

    Args:
        github_username (str): The GitHub username
        repository (str): The repository name
        notebook_filepath (str): The notebook filepath relative to the repository root
        branch (str, optional): The branch name. Defaults to 'master'.
    """
    display(
        HTML(
            create_jupyter_notebook_header(
                github_username, repository, notebook_filepath, branch
            )
        )
    )
