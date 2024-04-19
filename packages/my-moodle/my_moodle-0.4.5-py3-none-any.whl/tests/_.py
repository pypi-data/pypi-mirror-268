"""
Test
"""

import requests


def download_assignment_files(assignment_id, course_id):
    """Download assignment files from Moodle.

    Args:
        assignment_id (int): The assignment ID.
        course_id (int): The course ID.
    """
    # Assuming Moodle API endpoint for downloading files
    moodle_api_url = "https://moodle.midwest.tus.ie/webservice/rest/server.php?wstoken=2782900797a547bee925512d317f2987&moodlewsrestformat=json&wsfunction=mod_assign_get_submissions"

    # Make a request to Moodle API to retrieve file download links
    params = {"assignment_id": assignment_id, "course_id": course_id}
    response = requests.get(moodle_api_url, params=params, timeout=300.0)

    if response.status_code == 200:
        # Assuming the response contains download links for files
        file_links = response.json().get("file_links", [])

        # Download each file
        for file_link in file_links:
            file_name = file_link.split("/")[-1]  # Extract file name from the URL
            with open(file_name, "wb") as file:
                file_response = requests.get(file_link, timeout=300.0)
                file.write(file_response.content)
            print(f"File {file_name} downloaded successfully.")
    else:
        print("Failed to retrieve file download links from Moodle API.")


# Example usage
def main() -> None:
    """Main function."""
    assignment_id = 59462
    course_id = 10132
    download_assignment_files(assignment_id, course_id)
