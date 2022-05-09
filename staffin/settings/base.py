
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'ckeditor',
    'versatileimagefield',
    'djoser',

    'apps.user',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'staffin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'staffin.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'beebayk63478@gmail.com'
EMAIL_HOST_PASSWORD = 'ushivokopscgiscd'
EMAIL_USE_TLS = True

# ushivokopscgiscd
# beebayk63478@gmail.com


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    # 'DATE_FORMAT': '%b %d, %Y',
    # 'SEARCH_PARAM': 'q',
    # 'DEFAULT_PAGINATION_CLASS': 'nca.libs.drf.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 20,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    # 'EXCEPTION_HANDLER': 'nca.libs.drf.exceptions.exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
    ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'loginAttempts': '12/min',
    #     'user': '100/min',
    #     'burst': '5/min',
    #     'sustained': '50/day'
    # }
}

AUTH_USER_MODEL = 'user.User'


DJOSER = {
    'USER_ID_FIELD': 'id',
    'USER_CREATE_PASSWORD_RETYPE': True,
    # 'SEND_CONFIRMATION_EMAIL':  True,
    # 'SEND_ACTIVATION_EMAIL': True,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    # 'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    # 'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    # 'PASSWORD_RESET_CONFIRM_URL' : 'password-reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'PASSWORD_RESET_CONFIRM_URL': 'reset_password/{uid}/{token}',
    # 'USER_CREATE_USERNAME_RETYPE' : True,

    'SERIALIZERS': {
        'user': 'apps.user.serializers.UserListSerializer',
        'current_user': 'apps.user.serializers.UserDetailsSerializer',
        'token': 'apps.user.serializers.TokenSerializer',
        # 'activation': 'djoser.serializers.ActivationSerializer',
        # 'password_reset': 'djoser.serializers.SendEmailResetSerializer',
        # 'password_reset_confirm': 'djoser.serializers.PasswordResetConfirmSerializer',
        # 'password_reset_confirm_retype': 'djoser.serializers.PasswordResetConfirmRetypeSerializer',
        # 'set_password': 'djoser.serializers.SetPasswordSerializer',
        # 'set_password_retype': 'djoser.serializers.SetPasswordRetypeSerializer',
        # 'set_username': 'djoser.serializers.SetUsernameSerializer',
        # 'set_username_retype': 'djoser.serializers.SetUsernameRetypeSerializer',
        # 'username_reset': 'djoser.serializers.SendEmailResetSerializer',
        # 'username_reset_confirm': 'djoser.serializers.UsernameResetConfirmSerializer',
        # 'username_reset_confirm_retype': 'djoser.serializers.UsernameResetConfirmRetypeSerializer',
        # 'user_create': 'djoser.serializers.UserCreateSerializer',
        # 'user_create_password_retype': 'djoser.serializers.UserCreatePasswordRetypeSerializer',
        # 'user_delete': 'djoser.serializers.UserDeleteSerializer',
        # 'token_create': 'djoser.serializers.TokenCreateSerializer',

    }

}

VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'profile_picture': {
        ('listing', 'thumbnail__200x200'),
        ('details', 'crop__500x500'),
        ('full', 'url')
    }
}
