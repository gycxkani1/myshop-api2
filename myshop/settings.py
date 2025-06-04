from pathlib import Path
import os
import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kqpn@p8&y2m8*y#pqix0=^fda=%qwj$)1&x7lv2m@7#@*&*2$o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.basic',
    'apps.goods',
    'apps.order',
    'apps.users',

    'ckeditor',
    'ckeditor_uploader',

    'rest_framework',   # 用于API开发的Django REST框架
    'django_filters',  # 用于在视图中过滤数据的Django筛选器
    'rest_framework.authtoken',  # Django REST框架认证令牌中间件
    'rest_framework_swagger', # Django REST框架Swagger UI
    'corsheaders',  # CORS跨域请求的头部  
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # 用于处理跨域请求的中间件
    # 'django_prometheus.middleware.PrometheusBeforeMiddleware', # 用于监控Django应用程序的性能
    'django.middleware.security.SecurityMiddleware', # 安全中间件
    'django.contrib.sessions.middleware.SessionMiddleware', # 会话中间件
    'django.middleware.locale.LocaleMiddleware',  # 本地化中间件
    'django.middleware.common.CommonMiddleware', # 通用中间件
    'django.middleware.csrf.CsrfViewMiddleware', # 跨域请求伪造保护中间件
    'django.contrib.auth.middleware.AuthenticationMiddleware', # 用户认证中间件
    'django.contrib.messages.middleware.MessageMiddleware',  # 消息中间件
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # 点击劫持
    # 'common.middle.permmiddleware.PermissionMiddleWare', # 用中间件简化权限认证
    # 'django_prometheus.middleware.PrometheusAfterMiddleware', # 用于监控Django应用程序的性能
]

CORS_ALLOW_CREDENTIALS = True # 允许携带cookie跨域请求
CORS_ORIGIN_ALLOW_ALL = True # 允许所有来源的跨域请求
CORS_ORIGIN_WHITELIST = () # 跨域请求来源白名单

# 允许的跨域请求方法
CORS_ALLOW_METHODS  = [
     ' DELETE ',
     ' GET ',
     ' OPTIONS ',
     ' PATCH ',
     ' POST ',
     ' PUT ',
]
# 允许的跨域请求头部
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

ROOT_URLCONF = 'myshop.urls'

AUTH_USER_MODEL="users.MyUser"

#LOGIN_URL = '/diy_login/'  #这个路径需要根据你网站的实际登陆地址来设置

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media', # 添加媒体文件路径到上下文中
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shop_admin',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        #取消外键约束，否则多对多模型迁移报django.db.utils.IntegrityError: (1215, 'Cannot add foreign key constraint')
            'OPTIONS': {
            "init_command": "SET foreign_key_checks = 0;",
        }
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}

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

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/shanghai'

USE_I18N = True
USE_L10N = True

# USE_TZ = True
USE_TZ = False

STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/static')

MEDIA_URL="/media/"
MEDIA_DIR=os.path.join(BASE_DIR,"media")
MEDIA_ROOT=MEDIA_DIR

CKEDITOR_UPLOAD_PATH='upload/' # 上传文件的路径，默认在MEDIA_ROOT下
CKEDITOR_IMAGE_BACKEND='pillow' # 图片上传插件，需要安装pillow库
# 富文本编辑器ckeditor配置
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': (
            ['div', 'Source', '-', 'Save', 'NewPage', 'Preview', '-', 'Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Print', 'SpellChecker', 'Scayt'],
            ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat'],
            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField'],
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'ShowBlocks', '-', 'About', 'pbckcode'],
            ['Blockquote', 'CodeSnippet'],
        ),
        'width': 'auto',
    },
}


REST_FRAMEWORK = {
    # 全局分页配置
    #'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    #'PAGE_SIZE': 5,

    # 过滤器默认后端
    'DEFAULT_FILTER_BACKENDS': (
           'django_filters.rest_framework.DjangoFilterBackend',
    ),

    # 全局认证类
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 全局配置使用自定义的token认证
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication', # 配置验证方式为JWT验证
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',  
        # 'rest_framework.authentication.TokenAuthentication', # 使用Token令牌的HTTP身份认证
    ),

    # 全局权限配置
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',  # 需要登录认证才能访问
    ),

    # 全局渲染配置
    #'DEFAULT_RENDERER_CLASSES':(
    #    'common.customrender.CustomRender',
    #)

    #不然会提示 'AutoSchema' object has no attribute 'get_link'
    'DEFAULT_SCHEMA_CLASS':'rest_framework.schemas.coreapi.AutoSchema',

    # 自定义异常处理函数
    'EXCEPTION_HANDLER': 'common.customexception.custom_exception_handler'
}

# DRF扩展缓存时间
REST_FRAMEWORK_EXTENSIONS = {
    # 缓存时间，单位秒
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 10,
    # 缓存存储，与配置文件中的CACHES的键对应。
    'DEFAULT_USE_CACHE': 'default',
}

# JWT配置
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=3),  # Token 过期时间为3天
    'JWT_AUTH_HEADER_PREFIX': 'JWT',  # Token的头为：JWT XXXXXXXXXXXXXXXXXXXXXX
    'JWT_ALLOW_REFRESH': False,  # 是否允许刷新Token
    #自定义返回认证信息
    'JWT_RESPONSE_PAYLOAD_HANDLER':'common.jwt_utils.jwt_response_payload_handler'
}

# 自定义用户验证
AUTHENTICATION_BACKENDS = (
    'apps.users.views.CustomBackend',
)

#缓存配置
CACHES={
    'default':{
        'BACKEND':'django.core.cache.backends.db.DatabaseCache',
        'LOCATION':'my_cache_table',
    }
}

#CACHES = {
#    "default": {
#        "BACKEND": "django_redis.cache.RedisCache",
#        "LOCATION": "redis://192.168.77.101:6379",
#        "OPTIONS": {
#            "CLIENT_CLASS": "django_redis.client.DefaultClient",
#            "PASSWORD":"123456",
#        }
#    }
#}

