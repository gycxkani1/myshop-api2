from django.contrib import admin
from django.urls import path,include,re_path
from apps.users import views
from django.views.static import serve
from myshop import settings
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

user_list=views.MyUserViewSet.as_view({
    'get': 'list',
    'post':'create',
})

user_detail=views.MyUserDetailViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete':'destroy',
})


router.register('users',views.MyUserViewSet)

urlpatterns = [
    path('user_reg/', views.user_reg, name='user_reg'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('ajax_login_data/', views.ajax_login_data, name='ajax_login_data'),
    
    path('users/',user_list),
    path('users/<pk>/',user_detail), # 查找、更新、删除

    # path('users/',views.MyUserViewSet.as_view({'get': 'list', 'post': 'create'})), # 列表、创建
    # path('users/<pk>/',views.MyUserDetailViewSet.as_view({'get': 'retrieve','put': 'update','patch': 'partial_update','delete':'destroy',})), # 查找、更新、删除

    path('test/',views.test),
    # path("", include(router.urls))
]
#router.register('users', views.MyUserViewSet, basename="users")