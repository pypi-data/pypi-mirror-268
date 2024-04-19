"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Enrolled users fields Class
"""


class EnrolledUsersFields:
    """Class for the Enrolled users fields"""

    ID = "id"
    FULLNAME = "fullname"
    EMAIL = "email"
    ROLES = "roles"
    PROFILE_IMAGE_URL = "profileimageurl"
    LAST_COURSE_ACCESS = "lastcourseaccess"
    ROLE_SHORTNAME = "shortname"

    DEFAULT_PROFILE_IMAGE_URL = "/theme/image.php/catawesome/core/1708603678/u/f1"

    @classmethod
    def get_unwanted_fields(cls) -> set:
        """Get unwanted fields

        Returns:
            set: A set of unwanted fields
        """
        return {
            "username",
            "descriptionformat",
            "preferences",
            "country",
            "profileimageurlsmall",
            "description",
            "department",
            "idnumber",
            "enrolledcourses",
            "city",
            "roles",
        }

    @classmethod
    def get_field_order(cls) -> list:
        """Get field order for the CSV file

        Returns:
            list: A list of fields in the order they should appear in the CSV file
        """
        return [
            cls.ID,
            cls.FULLNAME,
            cls.EMAIL,
            cls.LAST_COURSE_ACCESS,
            cls.PROFILE_IMAGE_URL,
        ]
