from rest_framework import serializers
from .models import Customer
from Auth.serializer import UserSerializer



class CustomerProfileSerializer(serializers.ModelSerializer):
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


class CustomerOnCommentSerializer(serializers.ModelSerializer):
    # full_name = serializers.CharField(read_only=True)
    class Meta:
        model = Customer
        fields = ["id",'full_name','profile_pic']    
