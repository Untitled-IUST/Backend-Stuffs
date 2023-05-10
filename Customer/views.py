from django.shortcuts import render
from decimal import Decimal
from rest_framework.generics import RetrieveUpdateAPIView 
from .models import Customer
from Barber.models import Transaction
from .serializers import CustomerProfileSerializer,Customers, TransactionSerializer,  CustomerOnCommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
# Create your views here.

class CustomerProfileView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = Customers
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
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated],url_path="add_credits", url_name="add_credits")
    def add_credits(self, request):
        customer= Customer.objects.get(user_id=request.user.id)
        if request.method == 'PUT':
            added_credit = Decimal(request.data['credit'])
            if added_credit < 0:
                return Response({"error": "Credit cannot be negative"})        
            Transaction.objects.create(customer=customer, transaction_type='C', amount=added_credit)
            customer.credit += added_credit
            customer.save()
        serializer = CustomerOnCommentSerializer(customer)
        return Response(serializer.data)
        
        return Response({"credit":customer.credit})
    @action(detail=False, methods=['PUT'], permission_classes=[IsAuthenticated],url_path="decrease_credit", url_name="decrease_credit")
    def decrease_credit(self, request):
        customer= Customer.objects.get(user_id=request.user.id)
        credit = Decimal(request.data['credit'])
        if credit < 0:
            return Response({"error": "Credit cannot be negative"})
        if customer.credit < credit:
            return Response({"error": "Insufficient credit"})
        customer.credit -= credit
        customer.save()
        return Response({"credit":customer.credit})
    

# class TransactionsView(RetrieveAPIView):
#     queryset = Transaction.objects.all()

#     serializer_class = TransactionSerializer()
    # @action(detail=False, methods=("GET",), permission_classes=(IsAuthenticated,), url_path="transactions", url_name="transactions" )
    # def transactions(self, request):
    # customer= Customer.objects.get(user_id=request.user.id)
    # return Response(serializer.data)
    

class CustomerTransactionView(APIView):
    def get(self, request):
        customer = Customer.objects.get(user_id=request.user.id, )
        transactions = Transaction.objects.filter(customer_id=customer)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)