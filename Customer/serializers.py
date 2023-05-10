from rest_framework import serializers
from .models import Customer
from Barber.models import Transaction
from Auth.serializer import UserSerializer
from Barber.models import CategoryService


class Customers(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Customer
        fields = ['first_name','last_name','phone_Number','area','profile_pic','user']

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.phone_Number = validated_data.get('phone_Number',instance.phone_Number)
        instance.area = validated_data.get('area',instance.area)
        instance.profile_pic = validated_data.get('profile_pic',instance.profile_pic)
        instance.save()
        
        user_data = validated_data.pop('user', None)
        user = instance.user
        user_serializer = UserSerializer(user, data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        return instance


class CustomerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Customer
        fields = ['first_name','last_name','phone_Number','area','profile_pic','user', "credit"]


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['profile_pic'] = "https://amirmohammadkomijani.pythonanywhere.com" + representation['profile_pic']
        return representation
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.phone_Number = validated_data.get('phone_Number',instance.phone_Number)
        instance.area = validated_data.get('area',instance.area)
        instance.profile_pic = validated_data.get('profile_pic',instance.profile_pic)
        instance.save()
        
        user_data = validated_data.pop('user', None)
        user = instance.user
        user_serializer = UserSerializer(user, data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        return instance


class CustomerOnCommentSerializer(serializers.ModelSerializer):
    # full_name = serializers.CharField(read_only=True)
    # profile_pic = serializers.CharField(read_only=True)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['profile_pic'] = "https://amirmohammadkomijani.pythonanywhere.com" + representation['profile_pic']
        return representation    
    class Meta:
        model = Customer
        fields = ["id",'full_name','profile_pic']    
        read_only_fileds = ("id",'full_name','profile_pic',)
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name','last_name']
        
# class CustomerAddCreditSerializer(serializers.Serializer):
#     credit = serializers.DecimalField( max_digits=5, decimal_places=2, default=0.00)

class CategoryServiceSerializerOnTransactions(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.category')
    class Meta:
        model = CategoryService
        fields = ['service', 'price', 'servicePic', 'category',
                #   "barber"
                  ]

class TransactionSerializer(serializers.ModelSerializer):
    service = CategoryServiceSerializerOnTransactions()
    class Meta:
        model = Transaction
        fields = ("id", "transaction_type", "amount", "timestamp", "service")
        read_only_fields = ("id", "transaction_type", "amount", "timestamp", "service")
        # fields = "__all__" 

# class CustomerAddingCreditSerializer(serializers.Serializer):
#     customer_on_comment = CustomerOnCommentSerializer(read_only=True)
#     class Meta:
#         model = Customer
#         fields = ["credit"]
#         read_only_fields = ("customer_on_comment", )