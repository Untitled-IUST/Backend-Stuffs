from django.db import models
from django.conf import settings
from Auth.models import User
from Customer.models import Customer
import datetime
from dateutil.relativedelta import relativedelta
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError



class Barber(models.Model):

  area_chices = (
    ('Tehranpars','Tehranpars'),
    ('Nazi Abad','Nazi Abad'),
    ('Narmak','Narmak'),
    ('Tajrish','Tajrish'),
    ('Gheytariye','Gheytariye'),
    ('Marzdaran','Marzdaran'),
    ('Janat Abad','Janat Abad'),
    ('Vanak','Vanak'),
    ('Enghelab','Enghelab'),
    ('Valiasr','Valiasr'),
    ('Saadat Abad','Saadat Abad'),
    ('Piroozi','Piroozi'),
    ('Jordan','Jordan'),
  )

  gender_choices = (
    ('Male','Male'),
    ('Female','Female')
  )

  user = models.ForeignKey(
        User, on_delete=models.CASCADE,related_name='users',null=False)
  BarberShop = models.CharField(max_length=255,unique=False,null=False)
  Owner = models.CharField(max_length=255,null=False)
  Parvaneh = models.CharField(max_length=10,unique=True,null=True)
  phone_Number = models.CharField(max_length=11,unique = True,null=True)
  area = models.CharField(max_length=255,null=False,choices=area_chices)
  address = models.CharField(max_length=255,null=False)
  gender = models.CharField(max_length=6,choices=gender_choices,null=True)
  foundation = models.DateField(null=True)
  rate = models.FloatField(default=1,null=False)
  background = models.ImageField(upload_to='Barber/backg',null=False,default='default_profile.png')
  logo = models.ImageField(upload_to='Barber/Logo',null=False,default='default_profile.png')
  # expire_date = models.DateField(default=datetime.date.today() + relativedelta(months=1))

  # def save(self, *args, **kwargs):
  #     if not self.expire_date:
  #         self.expire_date = User.date_joined + relativedelta(months=1)
  #     super(Barber, self).save(*args, **kwargs)


class BarberDescription(models.Model):
  barber = models.ForeignKey(Barber,on_delete=models.CASCADE,related_name='barberDesc',null=True)
  title = models.CharField(max_length=40)
  description = models.TextField(max_length=256)
  img = models.ImageField(upload_to='Barber/Description',null=False,default='default_profile.png')


class BarberPremium(models.Model):
    
  during_choices = (
    (1,'1-month'),
    (3,'3-month'),
    (6,'6-month'),
    (12,'12-month'),
  )
  
  
  barber = models.ForeignKey(Barber,on_delete=models.CASCADE,default=1)
  expire_date = models.DateField(default=datetime.date.today() + relativedelta(months=1))
  month = models.IntegerField(choices=during_choices,default=0)




class Category(models.Model):
  
  # catg_choices = (
  #   ('hair','hair'),
  #   ('skin','skin'),
  #   ('makeup','makeup'),
  #   ('nail','nail'),
  # )
  
  category = models.CharField(max_length=20,null=False)
  barber = models.ForeignKey(Barber,on_delete=models.CASCADE,null=True,related_name='categories')


class CategoryService(models.Model):

  service = models.CharField(max_length=255,null=False)
  price = models.FloatField(null=False)
  servicePic = models.ImageField(upload_to='Barber/Service',null=False,default='default_profile.png')
  category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categoryServices')



class ServiceGallery(models.Model):
  service = models.ForeignKey(CategoryService,on_delete=models.CASCADE,related_name='gallery')
  img = models.ImageField(upload_to='Barber/Gallery',null=False,default='default_profile.png')

class OrderServices(models.Model):
  
  order_status = (
    ('ordering','ordering'),
    # ('confirmed','confirmed'),
    ('rejected','rejected'),
    ('paid','paid'),
    # ('BarberCancelled','BarberCancelled'),
    ('CustomerCancelled','CustomerCancelled'),
    ('Done','Done'),
  )
  
  service = models.ForeignKey(CategoryService,on_delete=models.CASCADE,related_name='services')
  customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer')
  barber = models.ForeignKey(Barber,on_delete=models.CASCADE,related_name='barber')
  time = models.TimeField()
  date = models.DateField(default=datetime.date.today)
  status = models.CharField(max_length=20,choices=order_status,default='ordering')
  quantity = models.IntegerField(default=1)
  # totalPrice = models.FloatField(default=0)
  
  def validate_unique(self, exclude=None):
        super().validate_unique(exclude)

        if self.status == 'confirmed':
            existing_records = OrderServices.objects.filter(
                barber=self.barber,
                time=self.time,
                date=self.date,
            ).exclude(status='confirmed').exclude(pk=self.pk)

            if existing_records.exists():
                conflicting_order = existing_records.first()
                if conflicting_order.status != 'confirmed':
                    raise ValidationError(
                        'A conflicting order with the same time already exists.'
                    )

  class Meta:
      unique_together = ('barber', 'time','date')
      ordering = ['date','time']


# class Comment(models.Model):
#   customer = models.ForeignKey(Customer,on_delete=models.CASCADE, related_name="authors_comments")
#   barber = models.ForeignKey(Barber,on_delete=models.CASCADE, related_name="comments")
#   body = models.TextField(max_length=1000,)
#   reply = models.TextField(max_length=1000,null=True, blank=True, default=None)
#   created_at = models.DateTimeField(auto_now_add=True)
#   # parent_comment = models.ForeignKey("self", null=True, default=None, on_delete=models.CASCADE, related_name="replies")
#   class Meta:
#     ordering = ['-created_at']
#   def __str__(self):
#     return f'{self.customer} Says:{self.body}; Reply:{self.reply}'  
#   # @property
#   # def children(self):
#       # return Comment.objects.filter(parent_comment=self).reverse()
#   # @property
#   # def is_parent(self):
#   #     if self.parent_comment is None:
#   #         return True
#   #     return False



class Rating(models.Model):
  barber= models.ForeignKey(Barber,on_delete=models.CASCADE, related_name="ratings")
  customer = models.ForeignKey(Customer,on_delete=models.CASCADE, related_name="authors_ratings")
  rating = models.PositiveSmallIntegerField ( validators=[MinValueValidator(1), MaxValueValidator(5)], null=False, default=3)
  created_at = models.DateTimeField(auto_now_add=True)
  class Meta:
    ordering = ['-created_at']
    unique_together = ('barber', 'customer')
  def __str__(self) -> str:
     return f"{self.customer} Rates {self.barber}:({self.rating})"


class Comments(models.Model):
  customer = models.ForeignKey(Customer,on_delete=models.CASCADE, related_name="authors_comments")
  barber = models.ForeignKey(Barber,on_delete=models.CASCADE, related_name="comments")
  body = models.TextField(max_length=1000,)
  created_at = models.DateTimeField(auto_now_add=True)
  class Meta:
    ordering = ['-created_at']
  def __str__(self):
    return f'[{self.id}]{self.customer} Says:{self.body};'  

class Reply(models.Model):
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name="replies",null=True )
    created_at = models.DateTimeField(auto_now_add=True,)
    text_body = models.TextField(max_length=1000,default="comment-reply")   
