from datetime import timedelta
from pathlib import Path
from environ import Env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
dot_env_path = BASE_DIR / ".env"
if dot_env_path.exists():
    with dot_env_path.open(encoding="utf-8") as f:
        env.read_env(f, overwrite=True)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY", default="---- SECRET KEY ----")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

# Application definition

INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third apps
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
    # local apps
    'streetanimal',  # 유기동물
    'accounts',  # 계정
    'adopt_assignment',  # 입양 신청
    'adopt_review',  # 입양 후기 게시판
    'inquiry_board',  # 문의 게시판
    'notice',  # 공지사항
]

if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
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


if DEBUG:
    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ] + MIDDLEWARE


ROOT_URLCONF = 'metabusDjango.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "metabusDjango" / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = 'metabusDjango.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        # mariadb setting
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'metabusA',  # DB 이름
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': ''

    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'accounts.User'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


INTERNAL_IPS = ['127.0.0.1']

CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=["http://localhost:3000"])
# CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS",
#                                 default=['http://localhost:3000'])

# djangorestframework

# 인증을 지원하는 방법으로서 뭘쓸거야 ? Session방법이랑 authentication방법을 쓸거야

# 환경변수 설정 (DAYs니까 숫자! )-> env.int로 정수형으로 바꿔야 함
# 운영하다가도 정책이 바뀔 수 있음
ACCESS_TOKEN_LIFETIME_DAYS = env.int("ACCESS_TOKEN_LIFETIME_DAYS", default=0)
ACCESS_TOKEN_LIFETIME_HOURS = env.int("ACCESS_TOKEN_LIFETIME_HOURS", default=0)
ACCESS_TOKEN_LIFETIME_MINUTES = env.int("ACCESS_TOKEN_LIFETIME_MINUTES", default=5)

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",

    ],

    # 원래 디폴트 만료 시간: 5분
    # 이렇게 위에 import 한 다음에 이렇게쓰면 ?
    # 새로 생성되는 토큰의 만료시간은 7일 뒤 !!
    'ACCESS_TOKEN_LIFETIME': timedelta(
        days=ACCESS_TOKEN_LIFETIME_DAYS,
        hours=ACCESS_TOKEN_LIFETIME_HOURS,
        minutes=ACCESS_TOKEN_LIFETIME_MINUTES,

    )

}

SIMPLE_JWT = {
    'USER_ID_FIELD': 'userID',
}


