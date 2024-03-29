from django.urls import path
from . import views
## when we use ModelViewSet we should implement urls with routers
from rest_framework_nested import routers as nested
from rest_framework import routers 


nestedRouter = nested.DefaultRouter()
router = routers.SimpleRouter()


#########################
### 1/ Barber panel urls


nestedRouter.register('categories', views.addCategoryView, basename='categories')
service_router = nested.NestedSimpleRouter(nestedRouter, 'categories', lookup='category')
service_router.register('service', views.addCategoryServiceView, basename='services')

router.register('profile',views.BarberProfileView,basename='profile')
router.register('description',views.BarberDescriptionView,basename='description')
router.register('panel',views.BarberPanelView,basename='Panel')
router.register('buypremium',views.BarberBuyPremiumView,basename='buypremium')



### 2/ Customer ordering and paying process urls
nestedRouter.register('info',views.BarberInfoView,basename='info')
router.register('area',views.Areas,basename='show areas')
router.register('order',views.OrderServiceView,basename='order')
router.register('basket',views.CustomerBasketView,basename='Basket')
router.register('OrderHistory',views.CustomerOrderHistoryView,basename='OrderHistory')


urlpatterns = \
    [
    path('comments/create/', views.CommentCreateAPIView.as_view(), name='comment-create'),
    path('comments/<int:pk>/reply/', views.CommentReplyAPIView.as_view(), name="comment-reply"),
    path('show-comments/', views.CommentShowAPIView.as_view(), name="comment-show"),
    path('premium/', views.BarberPremiumView.as_view(), name="premium"),
    path('premium/<int:pk>/', views.BarberPremiumView.as_view(), name="premium"),
    ] + \
        router.urls + nestedRouter.urls + service_router.urls