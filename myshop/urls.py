from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static 
from django.utils.translation import gettext_lazy as _

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPICodec
schema_view=get_schema_view(title='我的商城接口文档', renderer_classes=[SwaggerUIRenderer, OpenAPICodec])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basic/',include('apps.basic.urls')),
    path('goods/',include('apps.goods.urls')),
    path('order/',include('apps.order.urls')),
    path('users/',include('apps.users.urls')),

    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('api-jwt-auth/', obtain_jwt_token),
    path('docs/', include_docs_urls(title="我的商城")),
    path('docs2/', schema_view, name='docs'),
    path('', include('django_prometheus.urls')),
    # path('ckeditor/',include('ckeditor_uploader.urls')),
    # re_path('media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
    # re_path('static/(?P<path>.*)', serve, {"document_root": settings.STATIC_ROOT}),
] + staticfiles_urlpatterns()+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# else:
#     # urlpatterns += [path('^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
#     # path('^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT})]

#     urlpatterns += [re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
# re_path('static/(?P<path>.*)', serve, {'document_root': settings.STATIC_ROOT}),]

# 添加i18n URL配置
# urlpatterns += [
#     path(_('^i18n/'), include('django.conf.urls.i18n')),
# ]

