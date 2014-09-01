from django.core.exceptions import ValidationError


def validate_subject(vv):
    if "foo" in vv:
        raise ValidationError(
            "your subject is broke",
            code="validate_subject")
