from django.core.exceptions import ValidationError


def title_does_not_start_with_quote(vv):
    if vv[0] == '"' or vv[0] == "'":

        raise ValidationError(
            "Titles must not start with quotes",
            code="title_does_not_start_with_quote")


def title_bad_chars(vv):
    bad_chars = ["&", "<", ">"]

    for ch in bad_chars:
        if ch in vv:
            raise ValidationError(
                "Titles may not use &, <, or > chars",
                code="title_bad_chars")
