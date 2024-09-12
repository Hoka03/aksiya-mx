from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from src.apps.general.variables import COMPANY_VIDEO_MAX_SIZE, COMPANY_LOGO_MAX_SIZE, COMPANY_BANNER_MAX_SIZE


def validate_company_video_size(video_file):
    """
    CUSTOM VALIDATOR TO CHECK THE MAX MB OF VIDEO.
    """
    if video_file.size > COMPANY_VIDEO_MAX_SIZE:
        raise ValidationError(_("Max size error. Max size video 15MB."))


def validate_company_logo_size(logo):
    """
    CUSTOM VALIDATOR TO CHECK THE MAX MB OF LOGO.
    """
    if logo.size > COMPANY_LOGO_MAX_SIZE:
        raise ValidationError(_("Max size error. Max size logo 7MB."))


def validate_company_banner_size(banner):
    """
    CUSTOM VALIDATOR TO CHECK THE MAX MB OF BANNER.
    """
    if banner.size > COMPANY_BANNER_MAX_SIZE:
        raise ValidationError(_("Max size error. Max size banner 10MB."))