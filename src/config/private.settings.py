"""
Private settings that aren't to be stored in the repository.

This file should be copied to private.settings.py and 
your values entered there.  That file will then be 
merged into the final settings.py file by the configure.py
script.

This is to prevent sensitive information from being stored
in the repository, presenting a security risk.

Settings such as email credentials should go in this file.
However, I think I would like to make this optional, and
be prompted for the fields by the configure.py script, in
the same manner as the other fields.

Settings such as ALLOWED_HOSTS should be set in this file,
as they may differ between different development and 
production machines.

Obviously, these fields should also be available via the
admin panel, along with several other application options.
"""

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]

DEFAULT_FROM_EMAIL = 'tcjmealplanner@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'tcjmealplanner@gmail.com'
EMAIL_HOST_PASSWORD = '010744gc;'
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEFAULT_TITLE = 'The Code Jerk - Django/Bootstrap Template'