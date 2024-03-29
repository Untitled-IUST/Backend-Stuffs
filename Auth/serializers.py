from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer , UserSerializer as BaseUserSerializer
from .models import User
from rest_framework import serializers
from Barber.models import Barber
from Customer.models import Customer

class UserCreateSerializer(BaseUserCreateSerializer):
    
    # def save(self, **kwargs):
    #     user = super().save(**kwargs)
    #     if user.role == "barber":
    #         Barber.objects.create(user_id=user.id)
    #     elif user.role == "customer":
    #         Customer.objects.create(user=user)
        
    
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','username','email','role','password']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['email','username','password']





# from rest_framework import serializers
# from .models import Customer, Barber
# from rest_framework_simplejwt.tokens import RefreshToken


# class CustomerCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ['first_name','last_name','phone_Number','email','gender','password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         customer = Customer.objects.create_user(**validated_data)
#         return customer

# class BarberCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Barber
#         fields = ['BarberShop','Owner','Parvaneh','phone_Number','email','address','password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         barber = Barber.objects.create_user(**validated_data)
#         return barber



# class CustomerTokenObtainPairSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only = True)

#     class Meta:
#         model = Customer
#         fields = ['email','password']

#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')

#         user = Customer.objects.filter(email=email).first()

#         if user and user.check_password(password):
#             refresh = RefreshToken.for_user(user)
#             return {'access': str(refresh.access_token), 'refresh': str(refresh)}
#         raise serializers.ValidationError('Invalid email or password')

# class BarberTokenObtainPairSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()

#     class Meta:
#         model = Barber
#         fields = ['email','password']

#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')

#         user = Barber.objects.filter(email=email).first()

#         if user and user.check_password(password):
#             refresh = RefreshToken.for_user(user)
#             return {'access': str(refresh.access_token), 'refresh': str(refresh)}
#         raise serializers.ValidationError('Invalid email or password')