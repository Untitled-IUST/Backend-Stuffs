from rest_framework import serializers
from .models import Barber,Rate, Comment, Rating ,OrderServices,CategoryService,Category 
from Customer.serializers import CustomerOnCommentSerializer
from Auth.serializer import UserSerializer
from Customer.serializers import CustomerSerializer
from Customer.models import Customer

class OrderServiceSerializer(serializers.ModelSerializer):
    # service_id = serializers.PrimaryKeyRelatedField(source='service', queryset=Service.objects.all())

    class Meta:
        model = OrderServices
        fields = ['id','service','barber', 'time','date','status']

    
    # def validate_time(self, barber_id):
    #     if OrderServices.objects.filter(barber_id = barber_id):
    #         if OrderServices.objects.only('time').exists():
    #             raise ValueError('this time has been set')
    
    
    def save(self, **kwargs):
        customer, created = Customer.objects.get_or_create(user_id=self.context['user_id'])
        # barber, created = Barber.objects.get_or_create(id=self.context['barber_id'])
        # service, created = Service.objects.get_or_create(id=self.context['service_id'])
        # self.validated_data.update({'customer': customer,'barber':barber,'service':service, **kwargs})
        self.validated_data.update({'customer':customer,**kwargs})
        order = OrderServices.objects.create(**self.validated_data)
        return order


class CategoryServiceSerializer(serializers.ModelSerializer):
    class Meta():
        model = CategoryService
        fields = ['id','service','price','servicePic']
    
    def save(self, **kwargs):
        (category,created) = Category.objects.get_or_create(id = self.context['category_id'])
        self.validated_data.update({'category':category,**kwargs})
        service = CategoryService.objects.create(**self.validated_data)
        return service


class CategorySerializer(serializers.ModelSerializer):
    categoryServices = CategoryServiceSerializer(many=True,read_only=True)
    class Meta():
        model = Category
        fields = ['id','category','categoryServices']
    
    def update(self, instance, validated_data):
        instance.category = validated_data.get('category',instance.category)
        instance.save()
        return instance
    
    def save(self, **kwargs):
        (barber,created) = Barber.objects.get_or_create(id=self.context['barber_id'])
        self.validated_data.update({'barber':barber,**kwargs})
        catg = Category.objects.create(**self.validated_data)
        return catg

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
    rating = serializers.SerializerMethodField(source= "get_rating")
    customers_rate = serializers.SerializerMethodField()
    # comments = serializers.SerializerMethodField()
    # rating = serializers.SerializerMethodField()
    # comment_body = serializers.CharField(write_only=True, required=False)
    categories = CategorySerializer(many=True)
    class Meta:
        model = Barber
        fields = ('id','BarberShop','Owner','phone_Number','area','address','rate', "rating",
                  "customers_rate", 'background','logo', 'comments',"categories" )# ,"comment_body", ]# "rating"]
        read_only_fields = ("id", "created_at", "BarberShop", "Owner", "phone_Number", "area", "address" ,
                            'background','logo',"comments", "rate", "rating", "customers_rate")
    def get_comments(self, obj):
        comments = obj.comments.all()
        serializer = CommentSerializer(comments, many=True, context=self.context)
        return serializer.data  
    def get_rating(self, obj):
        comments = obj.comments.all()
        if comments:
            ratings = [comment.rating for comment in comments]
            return sum(ratings) / len(ratings)
        return 0
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
    
    
    # services = ServiceSerializer(many=True)

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


class BarberAreasSerializer(serializers.ModelSerializer):
    class Meta():
        model = Barber
        fields = ['area']


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['barbershop','stars']




    



