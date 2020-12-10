import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class PasswordComplexityValidator(object):
    """Custom password complexity validator.

    To pass validation, passwords must contain at least three of:
    - uppercase characters
    - lowercase characters
    - numbers
    - special characters
    """

    HELP_TEXT = _(
        "Your password must contain at least 3 of: uppercase characters, "
        "lowercase characters, numbers, and special characters."
    )

    def validate(self, password, user=None):
        type_count = 0

        REGEXES = [
            # Regular expression for lowercase characters.
            "[a-z]",
            # Regular expression for uppercase characters.
            "[A-Z]",
            # Regular expression for numbers.
            "[0-9]",
            # Regular expression for special characters.
            "[^a-zA-Z0-9]",
        ]

        for regex in REGEXES:
            if re.search(regex, password) is not None:
                type_count += 1

        if type_count < 3:
            raise ValidationError(self.HELP_TEXT, code="notcomplex")

    def get_help_text(self):
        return self.HELP_TEXT
