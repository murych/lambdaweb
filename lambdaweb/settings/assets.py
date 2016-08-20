import os
import env
import paths


if env.DEV_ENV:
	# Absolute filesystem path to the directory that will hold user-uploaded files.
	# Example: "/home/media/media.lawrence.com/media/"
	MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
	MEDIA_ROOT = '/var/www/modularsettings/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
"""
2.5MB - 2621440
5MB - 5242880
10MB - 10485760
20MB - 20971520
50MB - 5242880
100MB 104857600
250MB - 214958080
500MB - 429916160
"""
CONTENT_TYPES = ['image']
MAX_UPLOAD_SIZE = '5242880'
MEDIA_URL = '/media/'

if env.DEV_ENV:
	# Absolute path to the directory static files should be collected to.
	# Don't put anything in this directory yourself; store your static files
	# in apps' "static/" subdirectories and in STATICFILES_DIRS.
	# Example: "/home/media/media.lawrence.com/static/"
	STATIC_ROOT = os.path.join(BASE_DIR, '../../static/')
else:
	STATIC_ROOT = '/var/www/modularsettings/static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
	# Put strings here, like "/home/html/static" or "C:/www/django/static".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	os.path.join(STATIC_ROOT, 'files'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
