from django.shortcuts import render
from .models import Customer
from .serializers import CustomerProfileSerializer,CustomerWalletSerializer, TransactionSerializer
from Barber.models import Transaction
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

# Create your views here.

class CustomerProfileView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerProfileSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (customer, created) = Customer.objects.get_or_create(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerProfileSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerProfileSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)




class WalletView(ModelViewSet):
    serializer_class = CustomerWalletSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        (customer,created) = Customer.objects.get_or_create(user_id = self.request.user.id)
        return Customer.objects.filter(id = customer)

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated],url_path="add_credits", url_name="add_credits")
    def add_credits(self, request):
            (customer,created)= Customer.objects.get_or_create(user_id=request.user.id)
            if request.method == 'PUT':
                added_credit = float(request.data['credit'])
                customer.credit += added_credit
                customer.save()
            serializer = CustomerWalletSerializer(customer)
            return Response(serializer.data)
    


class CustomerTransactionView(APIView):
    def get(self, request):
        customer = Customer.objects.get(user_id=request.user.id, )
        transactions = Transaction.objects.filter(customer_id=customer)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)