from rest_framework import serializers
from .models import Barber,Rate, Comment, Rating
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



class RatingSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.id')
    barber = serializers.ReadOnlyField(source='barber.id')

    class Meta:
        model = Rating
        fields = "__all__"
        read_only_fields = ("id", "created_at", "barber", "customer")
        # exclude = ("created_at",)
        
    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance
class BarberSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    rating = serializers.SerializerMethodField()
    customers_rate = serializers.SerializerMethodField()
    # comments = serializers.SerializerMethodField()
    # rating = serializers.SerializerMethodField()
    # comment_body = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = Barber
        fields = ['id','BarberShop','Owner','phone_Number','area','address','rate',"rating","customers_rate", 'background','logo', 'comments', ]# ,"comment_body", ]# "rating"]
        read_only_fields = ("id", "created_at", "BarberShop", "Owner", "phone_Number", "area", "address" ,'background','logo',"comments", "rate", "rating", "customers_rate")
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
    def get_rating(self,obj):
        ratings = obj.ratings.all()
        if ratings :
            ratings = [rating_instance.rating for rating_instance in ratings]
            # print(*ratings, sep = "\*n")
            return round(sum(ratings) / len(ratings), 2)
        else:
            return 3.33
    def get_customers_rate(self, obj):
        customer = self.context['request'].user.customer
        # print(customer, sep = "*****\n")
        try:
            rating = obj.ratings.filter(customer=customer).order_by("-created_at").first()
            # rating = Rating.objects.get(customer= customer, barber = obj)
            return rating.rating
        except:
            return 3.33
            
    # def create(self, validated_data):
    #     validated_data['customer'] = self.context['request'].user.customer
    #     return super().create(validated_data)
    
    
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




class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['barbershop','stars']



