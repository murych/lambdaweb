import env

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sitemaps',
	'bootstrap3',
	'easy_thumbnails',
	'django_markdown',
	'registry',
)

if env.DEV_ENV:
	# INSTALLED_APPS += (
	#     'debug_toolbar',
	# )
	pass
