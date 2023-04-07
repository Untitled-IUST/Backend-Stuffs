from django.urls import path
from . import views
## when we use ModelViewSet we should implement urls with routers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('info',views.BarberView)
router.register('rate',views.RateView)

urlpatterns = router.urls


# urlpatterns = [
#     path('info/<int:pk>/',BarberView.as_view(),name='Barber info'),
#     path('info/',BarbersView,name='Barbers info'),
#     path('rate/<int:pk>/',RateView.as_view(),name = 'Rate Barber'),
# ]