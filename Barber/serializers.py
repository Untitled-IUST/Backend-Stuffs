from rest_framework import serializers
from .models import Barber
from Auth.models import Barber as BarberModel_Auth


class BarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barber
        fields = ['BarberShop','Owner','phone_Number','address']
    
class CommentsOnBarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarberModel_Auth
        fields = ("customer", "body", "barber", "created_at", "parent_comment")
        read_only_fields = ( "created_at") 
        
