from cerberus import Validator
import re

password_regex = r"^(?=.*[A-Z])(?=.*[a-z]).{8,}$"
email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"


class ValidatorExtended(Validator):
    def _validate_valid_password(self, valid_password, field, value):
        """ Test the valid_password of a value.
        The rule's arguments are validated against this schema:
        {'type': 'boolean'}
        """
        if valid_password and not re.match(password_regex, value):
            self._error(field, "Password must contain at least 8 characters, one uppercase and one lowercase letter")

    def _validate_valid_email(self, email, field, value):
        """ Test the valid_email of a value.
        The rule's arguments are validated against this schema:
        {'type': 'boolean'}
        """
        if (email and not re.match(email_regex, value)):
            self._error(field, "Invalid email")
