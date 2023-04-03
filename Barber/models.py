from django.db import models



class Barber(models.Model):
  BarberShop = models.CharField(max_length=255)
  Owner = models.CharField(max_length=255)
  Parvaneh = models.CharField(max_length=10,unique=True)
  phone_Number = models.CharField(max_length=11,unique = True)
  email = models.EmailField(unique=True)
  address = models.CharField(max_length=255)

