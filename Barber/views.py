from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from .models import Barber
from .serializers import BarberSerializer




class BarberView(RetrieveAPIView):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer



