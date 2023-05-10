from django.db import models
from django.conf import settings
from Auth.models import User
from Customer.models import Customer 
from django.core.validators import MinValueValidator, MaxValueValidator

import datetime

  
class Rate(models.Model):
  barbershop = models.ForeignKey('Barber',on_delete=models.SET_NULL,null=True,related_name='barbers')
  stars = models.IntegerField()

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


  user = models.ForeignKey(
        User, on_delete=models.CASCADE,related_name='users',null=False)
  BarberShop = models.CharField(max_length=255,unique=True,null=False)
  Owner = models.CharField(max_length=255,null=False)
  Parvaneh = models.CharField(max_length=10,unique=True,null=False)
  phone_Number = models.CharField(max_length=11,unique = True,null=True)
  # email = models.EmailField(unique=True)
  area = models.CharField(max_length=255,null=False,choices=area_chices)
  address = models.CharField(max_length=255,null=False)
  rate = models.FloatField(default=1,null=False)
  background = models.ImageField(upload_to='Barber/backg',null=False,default='default_profile.png')
  logo = models.ImageField(upload_to='Barber/Logo',null=False,default='default_profile.png')
  def __str__(self):
    return f"Barber No.{self.pk}"


class Comment(models.Model):
  customer = models.ForeignKey(Customer,on_delete=models.CASCADE, related_name="authors_comments")
  barber = models.ForeignKey(Barber,on_delete=models.CASCADE, related_name="comments")
  body = models.TextField(max_length=1000, )
  created_at = models.DateTimeField(auto_now_add=True)
  parent_comment = models.ForeignKey("self", null=True, default=None, on_delete=models.CASCADE, related_name="replies")
  # rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True, default=None)
  class Meta:
    ordering = ['-created_at']
  def __str__(self):
    return f'{self.customer} Says:{self.body}'  
  @property
  def children(self):
      return Comment.objects.filter(parent_comment=self).reverse()
  @property
  def is_parent(self):
      if self.parent_comment is None:
          return True
      return False




class Category(models.Model):
  
  catg_choices = (
    ('hair','hair'),
    ('skin','skin'),
    ('makeup','makeup'),
    ('nail','nail'),
  )
  
  category = models.CharField(choices=catg_choices,max_length=20)
  barber = models.ForeignKey(Barber,on_delete=models.CASCADE,null=True,related_name='categories')


class CategoryService(models.Model):
  service = models.CharField(blank=True,max_length=255)
  price = models.FloatField(default=0)
  servicePic = models.ImageField(upload_to='Barber/Service',null=True,default='default_profile.png')
  category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categoryServices')





class OrderServices(models.Model):
  
  order_status = (
    ('ordering','ordering'),
    ('ordered','ordered'),
    ('confirmed','confirmed'),
    ('paid','paid'),
  )
  
  service = models.ForeignKey(CategoryService,on_delete=models.CASCADE,related_name='services')
  customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer')
  barber = models.ForeignKey(Barber,on_delete=models.CASCADE,related_name='barber')
  time = models.TimeField()
  date = models.DateField(default=datetime.date.today)
  status = models.CharField(max_length=9,choices=order_status,default='ordering')
  class Meta:
      unique_together = ('barber', 'time','date')










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
    
    
class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('C', 'Charge'),
        ('O', 'Order'),
    )

    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, related_name="transactionCustomer")
    transaction_type =  models.CharField(max_length=1, choices=TRANSACTION_TYPES, default='C')
    amount = models.DecimalField( max_digits=5, decimal_places=2, default=0.00, blank=True,
                                 validators=(MinValueValidator(0.00), ))
    timestamp = models.DateTimeField( null=True,  blank=True , default=datetime.datetime.now())
    # order = models.ForeignKey(OrderServices, on_delete=models.CASCADE, related_name="transactionsOrder", null=True, default=None, blank=True)
    service = models.ForeignKey(CategoryService, on_delete=models.CASCADE, related_name= "transactionService", null=True,default=None, blank=True )
    class Meta:
        ordering = ['-timestamp',]
    def __str__(self) -> str:
        return f"{self.customer} Has {self.amount} Toman on {self.timestamp}"