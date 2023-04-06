from rest_framework import serializers
from .models import CustomerProfile
from Auth.models import Customer

# class CustomerProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomerProfile
#         fields = ['first_name','last_name','phone_Number','email']


class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name','last_name','phone_Number','email']