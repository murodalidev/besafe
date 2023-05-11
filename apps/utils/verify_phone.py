import os
from django.utils.translation import gettext_lazy as _


def get_sms_code(phone):
    if phone:
        # some code with sms provider
        return True
    return False


def verify_sms_code(phone, code):
    verification_code = os.environ.get('VERIFICATION_CODE', None)
    if code != verification_code:
        return False
    return True


