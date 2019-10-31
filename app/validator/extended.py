from cerberus import Validator


class ValidatorExtended(Validator):
    def _validate_contain_uppercase(self, contain_uppercase, field, value):
        if contain_uppercase and (value == value.lower()):
            self._error(field, "Password need contains at least one uppercase")

    def _validate_contain_lowercase(self, contain_lowercase, field, value):
        if contain_lowercase and (value == value.upper()):
            self._error(field, "Password need contains at least one lowercase")
