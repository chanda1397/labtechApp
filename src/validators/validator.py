from constants import PASSWORD_REGEX, ALPHA_REGEX, EMAIL_REGEX


def check_password(password):
    if not PASSWORD_REGEX.match(password):
        return False
    return True


def check_alpha(alpha):
    if not ALPHA_REGEX.match(alpha):
        return False
    return True


def check_email(email):
    if not EMAIL_REGEX.match(email):
        return False
    return True
