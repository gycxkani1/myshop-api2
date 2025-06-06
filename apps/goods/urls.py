from django.urls import path,include
from apps.goods import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
goods_category_list=views.GoodsCategoryViewset.as_view({'get':'list',})

goods_category_detail=views.GoodsCategoryViewset.as_view({ 'get': 'retrieve',})

indexgoods=views.IndexCategoryGoodsViewSet.as_view({ 'get':'list',})

# router=DefaultRouter()
router.register('goods',views.GoodsView)
router.register('slide',views.SlideViewset)

urlpatterns = [
    #GenericViewSet
    path('goodscategory/',goods_category_list),
    path('goodscategory/<pk>/',goods_category_detail),
    path('indexgoods/',indexgoods),
    #router.register('indexgoods',views.IndexCategoryViewset,basename="indexgoods"),
    path("",include(router.urls))
]
