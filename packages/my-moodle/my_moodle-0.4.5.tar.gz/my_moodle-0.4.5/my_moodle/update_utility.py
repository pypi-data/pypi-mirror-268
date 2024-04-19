"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Update utility
"""

import os
from os import makedirs
from os.path import join
import shutil
from requests import Response, get


def download_release(
    base_download_url: str, version: str, directory: str
) -> str | None:
    """Download the specified release from GitHub.

    Args:
        base_download_url (str): The base download URL
        version (str): The release version
        directory (str): The directory to save the zip file

    Returns:
        str: The path to the downloaded zip file
    """
    download_url = f"{base_download_url}/{version}.zip"
    response = get(download_url, timeout=5)
    if response.status_code == 200:
        return save_zip_file_to_temp_dir(response, version, directory)

    # Handle download failure
    print(f"Failed to download release {version}.")
    return None


def fetch_latest_release(api_url: str):
    """Fetch the latest release information from the GitHub API.

    Args:
        api_url (str): The GitHub API URL

    Returns:
        str: The latest release version
    """
    response = get(api_url, timeout=5)
    if response.status_code == 200:
        json_data = response.json()
        return json_data["tag_name"]

    print("Failed to fetch latest release information.")
    return None


def save_zip_file_to_temp_dir(response: Response, version: str, directory: str) -> str:
    """Save the downloaded zip file to the temporary directory.

    Args:
        response (Response): The response containing the data to save
        version (str): The release version
        directory (str): The directory to save the zip file

    Returns:
        str: The path to the new saved zip file
    """
    makedirs(directory, exist_ok=True)
    zip_file_path = join(directory, f"my-moodle-{version}.zip")
    with open(zip_file_path, "wb") as zip_file:
        zip_file.write(response.content)
    return zip_file_path


def extract_downloaded_zip(
    downloaded_file_path: str, version: str, download_directory: str
) -> str:
    """Extract the downloaded zip file to the temporary directory.

    Args:
        downloaded_file_path (str): The path to the downloaded zip file
        version (str): The release version

    Returns:
        str: The path to the extracted directory
    """
    extract_dir = os.path.join(download_directory, f"my-moodle-{version}")
    shutil.unpack_archive(downloaded_file_path, extract_dir, "zip")

    return os.path.join(extract_dir, f"my-moodle-template-{version}")


def update_application(
    api_url: str,
    app_directory_path: str,
    current_version: str,
    base_download_url: str,
    backup_dir: str,
    download_directory: str,
):
    """Update the application to the latest version.

    Args:
        api_url (str): The GitHub API URL
        app_directory_path (str): The path to the application directory
        current_version (str): The current version of the application
        base_download_url (str): The base download URL
        backup_dir (str): The backup directory
    """
    latest_version = fetch_latest_release(api_url)

    if not latest_version:
        print("Update failed: Unable to fetch latest release information.")
        return

    if latest_version == current_version:
        print("Application is already up to date.")
        return

    print(f"Latest version available: {latest_version}")
    downloaded_file_path = download_release(
        base_download_url, latest_version, download_directory
    )

    if not downloaded_file_path:
        print("Update failed: Unable to download release.")
        return

    try:
        extract_dir = extract_downloaded_zip(
            downloaded_file_path, latest_version, download_directory
        )

        move_directory_files(extract_dir, app_directory_path, backup_dir)

        print("Update successful.")
        shutil.rmtree(download_directory)
    except Exception as e:
        print(f"Update failed: {e}")
        return


def move_directory_files(
    source_dir: str, destination_dir: str, backup_dir: str
) -> None:
    """Move the files from the source directory to the destination directory.

    Args:
        source_dir (str): The source directory
        destination_dir (str): The destination directory
        backup_dir (str): The backup directory
    """
    os.makedirs(backup_dir, exist_ok=True)

    for item in os.listdir(source_dir):
        new_item = os.path.join(source_dir, item)
        original_item = os.path.join(destination_dir, item)
        backup_item = os.path.join(backup_dir, item)

        if os.path.isfile(new_item):
            shutil.move(original_item, backup_item)
            shutil.move(new_item, original_item)
    shutil.rmtree(backup_dir)


def update_my_moodle_template(app_directory_path, current_version) -> None:
    """Main function to update the application."""
    api_url = (
        "https://api.github.com/repos/marcocrowe/my-moodle-template/releases/latest"
    )
    backup_dir = "__backup"
    base_download_url = "https://github.com/marcocrowe/my-moodle-template/archive"
    temp_dir = "temp_update_dir"
    update_application(
        api_url,
        app_directory_path,
        current_version,
        base_download_url,
        backup_dir,
        temp_dir,
    )
