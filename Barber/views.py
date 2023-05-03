from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework import status
from .models import Barber,Rate, Comment,Rating
from Customer.models import Customer
from Auth.models import User
from Auth.serializer import UserSerializer
from .serializers import BarberSerializer,BarberProfileSerializer,RateSerializer, CommentSerializer, RatingSerializer
from .filters import BarberRateFilter
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist



class BarberView(ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BarberRateFilter
    search_fields = ['BarberShop']
    ordering_fields = ['rate']

    @action(methods=["POST",], permission_classes=[IsAuthenticated], detail=True)
    def add_coment(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        serializer.save(barber=self.get_object())
        return self.retrieve(request, *args, **kwargs)
    
    @action(methods=["POST"], permission_classes=[IsAuthenticated], detail=True)
    def rate(self, request,pk=None, *args, **kwargs):
        # Get all ratings for the specified barber and customer
        customer = request.user.customer
        barber = get_object_or_404(Barber, pk=pk)
        ratings = Rating.objects.filter(barber=barber, customer=customer)
        if ratings.exists():
            # If there are multiple ratings, delete all but the most recent one
            if ratings.count() > 1:
                old_ratings = ratings.order_by('-created_at')[:len(ratings)-1]
                # old_ratings.delete()
                for old_rating in old_ratings:
                    old_rating.delete()
            # Update the most recent rating with the new rating value
            rating =ratings.order_by('-created_at').first()
            serializer =RatingSerializer(rating, data=request.data)
        else :
                # If there are no ratings, create a new rating            
                serializer = RatingSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save(customer=customer, barber=barber)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Save the updated rating
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class BarberProfileView(ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberProfileSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (barber, created) = Barber.objects.get_or_create(
            user_id=request.user.id)
        # baseInfo = User.objects.prefetch_related('barber_set').all()
        if request.method == 'GET':
            serializer = BarberProfileSerializer(barber)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = BarberProfileSerializer(barber, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        

class RateView(ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
