from django.urls import path
from .views import BarberView, BarberDetail, CommentView


urlpatterns = [
    path('info/<int:pk>/',BarberView.as_view(),name='Barber info'),
    path("info2/<int:pk>/",BarberDetail.as_view(), name="Barber info with comments"),
    path("comments/<int:pk>/", CommentView.as_view(), name="all_comments"),
]