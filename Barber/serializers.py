from rest_framework import serializers
from .models import Barber,Rate, Comment
from Customer.serializers import CustomerOnCommentSerializer
from Auth.serializer import UserSerializer



# class BarberShopImagesSerializer(serializers.ModelSerializer):
    
#     def create(self, validated_data):
#         barbershop_id = self.context['barbershop_id']
#         return BarberShopImages.objects.create(barbershop_id=barbershop_id,**validated_data)
    
#     class Meta:
#         model = BarberShopImages
#         fields = ['background','logo']

class CommentSerializer(serializers.ModelSerializer):
    customer = CustomerOnCommentSerializer(read_only = True)
    replies = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("id", "created_at","customer" )
        # exclude = ("created_at")
    def get_replies(self, obj):
        replies = obj.replies.all()
        serializer = self.__class__(replies, many=True, context=self.context)
        return serializer.data        
    def create(self, validated_data):
        validated_data['customer'] = self.context['request'].user.customer
        return super().create(validated_data)
        
class BarberSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    # comments = serializers.SerializerMethodField()
    # rating = serializers.SerializerMethodField()
    # comment_body = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = Barber
        fields = ['id','BarberShop','Owner','phone_Number','area','address','rate','background','logo', 'comments']# ,"comment_body", ]# "rating"]
        read_only_fields = ("id", "created_at", "BarberShop", "Owner", "phone_Number", "area", "address" ,'background','logo',"comments", "rate")
    # def get_comments(self, obj):
    #     comments = obj.comments.all()
    #     serializer = CommentSerializer(comments, many=True, context=self.context)
    #     return serializer.data  
    # def get_rating(self, obj):
    #     comments = obj.comments.all()
    #     if comments:
    #         ratings = [comment.rating for comment in comments]
    #         return sum(ratings) / len(ratings)
    #     return 0
class BarberProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta():
        model = Barber
        fields = ['BarberShop','Owner','Parvaneh','phone_Number','area','address','background','logo','user',]


    def update(self, instance, validated_data):
        instance.BarberShop = validated_data.get('BarberShop',instance.BarberShop)
        instance.Owner = validated_data.get('Owner',instance.Owner)
        instance.Parvaneh = validated_data.get('Parvaneh',instance.Parvaneh)
        instance.phone_Number = validated_data.get('phone_Number',instance.phone_Number)
        instance.area = validated_data.get('area',instance.area)
        instance.address = validated_data.get('address',instance.address)
        instance.background = validated_data.get('background',instance.background)
        instance.logo = validated_data.get('logo',instance.logo)
        instance.save()
        
        user_data = validated_data.pop('user', None)
        user = instance.user
        user_serializer = UserSerializer(user, data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        return instance


    # def update(self,instance , validated_data):
        
    #     categories_data = validated_data.pop('categories')
    #     categories = instance.categories
    #     cate = []
    #     for data in categories_data:
    #         cate.append(models.Category.objects.get(name=data["name"]))
    #     categories.set(cate)

    #     instance.title = validated_data.get('title' , instance.title)
    #     instance.room_type = validated_data.get("room_type" , instance.room_type)
    #     instance.link = validated_data.get('link' , instance.link)
    #     instance.password = validated_data.get('password' , instance.password)
    #     instance.description = validated_data.get('description' , instance.description)
    #     instance.start_date = validated_data.get('start_date' , instance.start_date)
    #     instance.end_date = validated_data.get('end_date' , instance.end_date)
    #     instance.maximum_member_count = validated_data.get('maximum_member_count' , instance.maximum_member_count)
    #     instance.open_status = validated_data.get("open_status" , instance.open_status)
        
    #     instance.save()
        
    #     return instance


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['barbershop','stars']



