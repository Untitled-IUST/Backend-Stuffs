from django.db import models
from Auth.models import  Barber as BarberModel, Customer



class Barber(models.Model):
  BarberShop = models.CharField(max_length=255)
  Owner = models.CharField(max_length=255)
  Parvaneh = models.CharField(max_length=10,unique=True)
  phone_Number = models.CharField(max_length=11,unique = True)
  email = models.EmailField(unique=True)
  address = models.CharField(max_length=255)


class Comment(models.Model):
  customer = models.ForeignKey(Customer,on_delete=models.CASCADE, related_name="author_comments")
  barber = models.ForeignKey(BarberModel,on_delete=models.CASCADE, related_name="comments")
  body = models.TextField(max_length=1000)
  created_at = models.DateTimeField(auto_now_add=True)
  parent_comment = models.ForeignKey("self", null=True, default=None, on_delete=models.CASCADE, related_name="replies")
  class Meta:
    ordering = ['-created_at']
    
  def __str__(self):
    return f'"{self.body}" By: {self.customer}'
  

  @property
  def children(self):
      return Comment.objects.filter(parent_comment=self).reverse()

  @property
  def is_parent(self):
      if self.parent_comment is None:
          return True
      return False
  