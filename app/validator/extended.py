from cerberus import Validator
import re


class ValidatorExtended(Validator):
    def _validate_valid_password(self, valid_password, field, value):
        if valid_password and re.match(r"^(?=.*[A-Z])(?=.*[a-z]).{8,}$", value) is None:
            self._error(field, "Password must contain at least 8 characters, one uppercase and one lowercase letter")
