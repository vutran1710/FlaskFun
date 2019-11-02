from cerberus import Validator
import re


class ValidatorExtended(Validator):
    def _validate_contain_uppercase(self, contain_uppercase, field, value):
        if contain_uppercase and (value == value.lower()):
            self._error(field, "Password need contains at least one uppercase")

    def _validate_contain_lowercase(self, contain_lowercase, field, value):
        if contain_lowercase and (value == value.upper()):
            self._error(field, "Password need contains at least one lowercase")

    def _validate_valid_email(self, email, field, value):
        if (email and not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value)):
            self._error(field, "Invalid email")
