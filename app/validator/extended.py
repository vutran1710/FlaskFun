from cerberus import Validator
import re


class ValidatorExtended(Validator):
    def _validate_valid_password(self, valid_password, field, value):
        if valid_password and not re.match(r"^(?=.*[A-Z])(?=.*[a-z]).{8,}$", value):
            self._error(field, "Password must contain at least 8 characters, one uppercase and one lowercase letter")

    def _validate_valid_email(self, email, field, value):
        if (email and not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value)):
            self._error(field, "Invalid email")
