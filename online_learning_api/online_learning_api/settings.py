"""
Django settings for online_learning_api project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7gdi9of+54=t)6o*z449sv&!6#au_t6z-8=knknuc8z0_8-3lw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    #跨域
    'corsheaders',
    #用户认证
    # 'djoser',
    # 'drf_yasg',
    'django_filters',
    #富文本编辑器
    'mdeditor',
    'taggit',
    "apps.user",
    "apps.course",
    "apps.post",
    "apps.comment",
    "apps.cart",
    "apps.order",
    "apps.coupon"
]
X_FRAME_OPTIONS = 'SAMEORIGIN'  # django 3.0 + 默认为 deny

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ALLOWED_HOSTS = ["*"]
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]

ROOT_URLCONF = 'online_learning_api.urls'

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

WSGI_APPLICATION = 'online_learning_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'online_learning',
        'USER': 'lyx',
        'PASSWORD': 'lyx',
        'HOST': '120.26.205.152',
        'PORT': '3306',
        }
}

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "verbose": {
#             "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
#             "style": "{",
#         },
#         "simple": {
#             "format": "{levelname} {message}",
#             "style": "{",
#         },
#     },
#     "filters": {
#         "require_debug_true": {
#             "()": "django.utils.log.RequireDebugTrue",
#         },
#     },
#     "handlers": {
#         "console": {
#             "level": "INFO",
#             "filters": ["require_debug_true"],
#             "class": "logging.StreamHandler",
#             "formatter": "simple",
#         },
#         "file":{
#             "level": "INFO",
#             "class": "logging.handlers.RotatingFileHandler",
#             "filename": BASE_DIR / "logs/online_learning.log"
#         }
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["console", "file"],
#             "propagate": True,
#         },
#     },
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'user.User'


# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://:@120.26.205.152:6379/0",

#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "CONNECTION_POOL_KWARGS": {"max_connections": 100},
#         }
#     },
#     # 提供给admin运营站点的session存储
#     "session": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://:@120.26.205.152:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "CONNECTION_POOL_KWARGS": {"max_connections": 100},
#         }
#     },
#     # 提供存储短信验证码
#     "sms_code": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://:@120.26.205.152:6379/2",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "CONNECTION_POOL_KWARGS": {"max_connections": 100},
#         }
#     },
#     # 提供存存储热门关键字
#     "hot_word": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://:@120.26.205.152:6379/3",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     },
#     # 提供存储购物车课程商品
#     "cart": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://:@120.26.205.152:6379/4",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     },
# }
# 设置用户登录admin站点时,记录登录状态的session保存到redis缓存中
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 设置session保存的位置对应的缓存配置项
# SESSION_CACHE_ALIAS = "session"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter'
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),

    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
}

# AUTHENTICATION_BACKENDS = [
#     'common.authentication.MyBackend'
# ]

# source E:/python/online_learning_api/Scripts/activate 
