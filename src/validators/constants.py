from re import compile
EMAIL_REGEX = compile(r"\"?([-a-zA-Z0-9._?{}]+@\w+\.\w+)\"?")
PASSWORD_REGEX = compile(r'^([\w!\-#@&%]{8,})$')
ALPHA_REGEX = compile(r'^([a-zA-z-\']+)$')
