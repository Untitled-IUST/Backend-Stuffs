from django.db import models

  
class Rate(models.Model):
  barbershop = models.ForeignKey('Barber',on_delete=models.SET_NULL,null=True,related_name='barbers')
  stars = models.FloatField()

class Barber(models.Model):
  # profile_img = models.ImageField(upload_to='images/')
  BarberShop = models.CharField(max_length=255,unique=True)
  Owner = models.CharField(max_length=255)
  Parvaneh = models.CharField(max_length=10,unique=True)
  phone_Number = models.CharField(max_length=11,unique = True)
  email = models.EmailField(unique=True)
  address = models.CharField(max_length=255)
  rate = models.FloatField()

  # def update_rate(self):
  #     avg_stars = Rate.objects.filter(barbershop=self).aggregate(avg_rate=Avg('stars'))['avg_rate']
  #     self.rate = round(avg_stars, 2) if avg_stars else 1
  #     self.save()

