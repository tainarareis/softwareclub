"""
Django settings for softwareclub project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9@-s3$nk$86k($px2s*w8)j-@nfh0qayavz&)998c+t4**k#&n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'perfis',
    'usuarios',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)

LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   #'social.backends.github.GithubOAuth2',
   'django.contrib.auth.backends.ModelBackend',
)

# Tutorial: http://artandlogic.com/2014/04/tutorial-adding-facebooktwittergoogle-authentication-to-a-django-application/
SOCIAL_AUTH_FACEBOOK_KEY = 1612541262409392
SOCIAL_AUTH_FACEBOOK_SECRET = '8a234cbbb1184625358e4fc301157c97'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '817515988241-r0dprs4qjcp44d0s7etknl7rag428hve.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '6NpmKHbetr_hO_nFk7H11hAY'

SOCIAL_AUTH_TWITTER_KEY =  'M7EJhej2Iur0Ymh3gDCilHode'
SOCIAL_AUTH_TWITTER_SECRET = 	'G6yfh2vxmku8REVzV01FwcgB8iMQiHM36Nm1hLTcCw2mgMNuJi'

# Tutorial: http://django-social-auth.readthedocs.io/en/latest/backends/github.html
# GITHUB_APP_ID = 'e7864a83f5d718aa2177'
# GITHUB_API_SECRET = 'f419087541d0200a96ea618cd2d6c729340ffecd'

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.user.update_user_details',
    'auth_pipelines.pipelines.get_user_avatar',
    'usuarios.pipeline.salvar_perfil',
)

ROOT_URLCONF = 'softwareclub.urls'

WSGI_APPLICATION = 'softwareclub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL="/login/"
LOGOUT_URL="/logout/"
#LOGIN_REDIRECT_URL="/index"
