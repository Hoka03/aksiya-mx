from django import template

register = template.Library()

@register.filter(name='length_is')
def length_is(value, arg):
    """
    Checks if the length of the value is equal to the argument.
    :param value: The value whose length is to be checked.
    :param arg: The length to compare against.
    :return: Boolean result of the comparison.
    """
    try:
        return len(value) == int(arg)
    except (ValueError, TypeError):
        return False
