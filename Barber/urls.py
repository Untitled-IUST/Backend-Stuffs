from django.urls import path
from .views import BarberView, BarberDetail


urlpatterns = [
    path('info/<int:pk>/',BarberView.as_view(),name='Barber info'),
    path("info2/<int:pk>/",BarberDetail.as_view(), name="BarberView by Faraz"),
]