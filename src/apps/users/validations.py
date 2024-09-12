from rest_framework.exceptions import ValidationError


def phone_validate(phon_number: str):
    if not (len(phon_number) == 13
        |
        phon_number.startswith('+998')
        |
        phon_number[1:].isdigit()):
        raise ValidationError('Phone number was entered mistake.'
                              'Please try again.')