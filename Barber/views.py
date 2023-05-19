from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Barber,OrderServices,Category,CategoryService,BarberDescription
from .serializers import BarberInfoSerializer,BarberProfileSerializer,BarberAreasSerializer,OrderServiceSerializer,CategorySerializer,BarberDescriptionSerializer,CategoryServiceSerializer,Get_CustomerBasketSerializer,Put_CustomerBasketSerializer,Put_BarberPanelSerializer,Get_BarberPanelSerializer
from .filters import BarberRateFilter,BarberPanelFilter
from rest_framework.permissions import IsAuthenticated
from Customer.models import Customer




#######################################################
### Barber Panel Serializers

## 1/ adding category and service

class addCategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    def get_serializer_context(self):
        return {'barber_id':self.request.user.id}

    def get_queryset(self):
        (barber,created) = Barber.objects.get_or_create(user_id = self.request.user.id)
        return Category.objects.filter(barber_id = barber)


class addCategoryServiceView(ModelViewSet):
    serializer_class = CategoryServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'category_id':self.kwargs['category_pk']}

    def get_queryset(self):
        (category,created) = Category.objects.get_or_create(id=self.kwargs['category_pk'])
        return CategoryService.objects.filter(category_id = category)


## 2/ profile and description of barbershop

class BarberProfileView(ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberProfileSerializer

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (barber, created) = Barber.objects.get_or_create(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = BarberProfileSerializer(barber)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = BarberProfileSerializer(barber, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        

class BarberDescriptionView(ModelViewSet):
    serializer_class = BarberDescriptionSerializer

    def get_queryset(self):
        (barber,created) = Barber.objects.get_or_create(user_id = self.request.user.id)
        return BarberDescription.objects.filter(barber_id = barber)
    def get_serializer_context(self):
        return {'barber_id':self.request.user.id}


## 3/ Barber management segment

class BarberPanelView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = BarberPanelFilter
    ordering_fields = ['date','time']

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return Put_BarberPanelSerializer
        return Get_BarberPanelSerializer
    
    def get_queryset(self):
        (barber,created) = Barber.objects.get_or_create(user_id = self.request.user.id)
        return OrderServices.objects.filter(barber_id = barber)




#######################################################
### customer ordering and paying process
## 1/ Barber info

class BarberInfoView(ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberInfoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BarberRateFilter
    search_fields = ['BarberShop']
    ordering_fields = ['rate']


## 2/ Ordering a service

class OrderServiceView(ModelViewSet):
    serializer_class = OrderServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    
    def get_queryset(self):
        (customer,created) = Customer.objects.get_or_create(user_id=self.request.user.id)
        return OrderServices.objects.filter(customer_id = customer)

## 3/ Customer Basket

class CustomerBasketView(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return Put_CustomerBasketSerializer
        return Get_CustomerBasketSerializer
    def get_queryset(self):
        (customer,created) = Customer.objects.get_or_create(user_id=self.request.user.id)
        return OrderServices.objects.filter(customer_id = customer)





###############################################################
### extra information    

class Areas(ModelViewSet):
    serializer_class = BarberAreasSerializer
    pagination_class=None

    def get_queryset(self):
        return Barber.objects.values('area').distinct()



