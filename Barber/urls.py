from django.urls import path
from .views import BarberView


urlpatterns = [
    path('info/<int:pk>/',BarberView.as_view(),name='Barber info'),
    
]