from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import Barber,Rate
from .serializers import BarberSerializer,RateSerializer



class BarberView(ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['address','rate']
    search_fields = ['BarberShop']
    ordering_fields = ['rate']

# class BarberView(ModelViewSet):
#     queryset = Barber.objects.all()
#     serializer_class = BarberSerializer


class RateView(ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
