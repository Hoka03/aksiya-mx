from PIL import Image
from django.core.exceptions import ValidationError


def validate_image_size(image):
    """
    CUSTOM VALIDATOR TO CHECK THE UPLOAD IMAGE.
    """
    img = Image.open(image)
    max_width = 500
    max_height = 250

    if img.width > max_width or img.height > max_height:
        raise ValidationError(f"Image dimensions should not exceed"
                              f" {max_width}px in width and {max_height}px in height.")


def validate_banner_size(banner):
    """
    CUSTOM VALIDATOR TO CHECK THE UPLOAD BANNER.
    """
    _banner = Image.open(banner)
    max_width = 1000
    max_height = 500

    if _banner.width > max_width or _banner.height > max_height:
        raise ValidationError(f"Banner dimensions should not exceed"
                              f" {max_width}px in width and {max_height}px in height.")


def validate_logo_size(logo):
    """
    CUSTOM VALIDATOR TO CHECK THE UPLOAD LOGO.
    """
    _logo = Image.open(logo)
    max_width = 100
    max_height = 50

    if _logo.width > max_width or _logo.height > max_height:
        raise ValidationError(f"Logo dimensions should not exceed"
                              f" {max_width}px in width and {max_height}px in height.")


def validate_icon_size(icon):
    """
    CUSTOM VALIDATOR TO CHECK THE UPLOAD ICON.
    """
    _icon = Image.open(icon)
    max_width = 50
    max_height = 25

    if _icon.width > max_width or _icon.height > max_height:
        raise ValidationError(f"Icon dimensions should not exceed"
                              f" {max_width}px in width and {max_height}px in height.")