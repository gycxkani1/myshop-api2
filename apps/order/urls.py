from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from apps.order import views

router=DefaultRouter()
router.register('cart',views.CartViewset,basename="cart")
router.register('orderdetail',views.OrderDetailViewSet,basename="orderdetail")


urlpatterns = [
    #GenericViewSet
    path('order/',views.OrderView.as_view()),#get，Post
    path('orderlist/',views.OrderViewset.as_view({'get': 'list','post':'create',})),
    path("",include(router.urls))
]