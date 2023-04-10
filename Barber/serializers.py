from rest_framework import serializers
from .models import Barber, Comment
from Auth.models import Barber as BarberModel_Auth, Customer


class BarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barber
        fields = ['BarberShop','Owner','phone_Number','address']
    

class CustomerSerializer(serializers.ModelSerializer): 
    # Serializer for the customer field in the Comment model
    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name", "profile_picture")

class CommentSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = Comment
        fields = "__all__"
class CommentSerializerOnPOST(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        exlude = ("created_at",)
    
        
class BarberWithCommentsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True)
    class Meta:
        model = BarberModel_Auth
        fields =['BarberShop','Owner','phone_Number','address', "comments"]
        read_only_fields = ( "created_at",) 
