from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet,ViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from .models import Barber,Rate,Service,OrderServices, Rating
from .serializers import BarberSerializer,BarberProfileSerializer,RateSerializer,ServiceSerializer,\
                        CreateServiceSerializer,BarberAreasSerializer,OrderServiceSerializer, CommentSerializer, RatingSerializer
from .filters import BarberRateFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from Auth.models import User
from Customer.models import Customer




# class OrderServiceView(ModelViewSet):
#     queryset = OrderServices.objects.all()
#     serializer_class = OrderServiceSerializer
#     permission_classes = [IsAuthenticated]

#     # def get_queryset(self):
#     #     return OrderServices.objects.filter(service_id = self.kwargs['pk'])

#     def get_serializer_context(self):
#         return {'user_id':self.request.user.id,'barber_id':self.kwargs['info_pk'],'service_id':self.kwargs['pk']}


class OrderServiceView(ModelViewSet):
    # queryset = OrderServices.objects.all()
    serializer_class = OrderServiceSerializer
    permission_classes = [IsAuthenticated]


    # def create(self, request, *args, **kwargs):
    #     serializer = OrderServiceSerializer(data=request.data,
    #         context={'user_id':self.request.user.id})
    #     serializer.is_valid(raise_exception=True)
    #     order = serializer.save()
    #     serializer = OrderServiceSerializer(order)
    #     return Response(serializer.data)

    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    
    def get_queryset(self):
        (customer,created) = Customer.objects.get_or_create(user_id=self.request.user.id)
        return OrderServices.objects.filter(customer_id = customer)




class BarberView(ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BarberRateFilter
    search_fields = ['BarberShop']
    ordering_fields = ['rate']
    # permission_classes = [IsAuthenticated]
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


class Areas(ModelViewSet):
    serializer_class = BarberAreasSerializer

    def get_queryset(self):
        return Barber.objects.only('area')



class addService(ModelViewSet):
    # queryset = Service.objects.all()
    # serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateServiceSerializer
        return ServiceSerializer

    def get_queryset(self):
        (barber,created) = Barber.objects.only('id').get_or_create(user_id = self.request.user.id)
        return Service.objects.filter(barber_id = barber).all()
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}


        
class RateView(ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer



