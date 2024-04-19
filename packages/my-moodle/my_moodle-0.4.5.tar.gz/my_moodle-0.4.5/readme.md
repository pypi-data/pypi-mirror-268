
# [My Moodle](https://pypi.org/project/my-moodle/ "My Moodle")

A Python package to download data from Moodle.

## Sample Usage

The following is a sample usage of the package:

```python

%pip install my-moodle

from my_moodle import (ConfigUtility, MoodleDataDownloader)

def main() -> None:
    """Main function"""

    program, server, token = ConfigUtility.check_and_read_config()

    moodle_data_downloader: MoodleDataDownloader = MoodleDataDownloader(
        program, server, token, data_dir=""
    )
    moodle_data_downloader.download_my_data()


# Call the main function
if __name__ == "__main__":
    main()
```

## Get Moodle Token

Using <https://moodle.maynoothuniversity.ie> as an example:

1. Open <https://moodle.maynoothuniversity.ie/user/managetoken.php>
2. Copy the key for Moodle mobile web service.
3. Place it in file [config.ini](config.ini)

```ini
[App]
program = Content Management Systems
server = https://moodle.maynoothuniversity.ie
token = INSERT_YOUR_TOKEN # e.g. 63c1774a3eaf47db816c57ba1abafd40
```

*Note: The token is a secret key, do not share it with anyone.*

---
Copyright &copy; 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
