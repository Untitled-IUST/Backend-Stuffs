from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Group,Permission,AbstractUser
from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator,EmailValidator, int_list_validator


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email field is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Customer(AbstractBaseUser, PermissionsMixin):
  
  Gender_Choices = [
    ('M','Male'),
    ('F','Female'),
  ]
  
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  # phone_Number = models.CharField(max_length=11,unique=True)
  phone_Number = models.CharField(max_length=11,unique = True, 
                                  validators=[ 
                                              # MinLengthValidator(11, message="Phone No. must have 11 numeric characters."),
                                              # int_list_validator(sep = '', message="phone No. is not valid"),
                                              ])
  email = models.EmailField(unique=True)
  gender = models.CharField(max_length=6,choices=Gender_Choices)
  password = models.CharField(max_length=255, validators=[
                                                          # MinLengthValidator(8, message="Password must have at least 8 characters."),
                                                          # MaxLengthValidator(15, message="password must have at most 15 characters."),
                                                          ])
  # password = models.CharField(
  #       max_length=15,
  #       validators=[
            # RegexValidator(
            #     regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
            #     message='Password must contain at least 8 characters, including at least 1 uppercase letter, 1 lowercase letter, 1 special character and 1 numeric character'
            # ),
      #       MinLengthValidator(8)
      #   ]
      # )
  objects = CustomUserManager()

#   USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = ['first_name', 'last_name']
    
  groups = models.ManyToManyField(
        Group,
        related_name='customer_groups'
    )
  user_permissions = models.ManyToManyField(
        Permission,
        related_name='customer_user_permissions'
    )
  

    
    
class Barber(AbstractBaseUser, PermissionsMixin):
  BarberShop = models.CharField(max_length=255)
  Owner = models.CharField(max_length=255)
  Parvaneh = models.CharField(max_length=10,unique=True,validators=[
                                                                    # MinLengthValidator(10, message = "Parvaneh No. must be 10 numbers"),
                                                                    # int_list_validator(sep='', message = "Parvaneh No. is not  valid.")
                                                                    ])
  # phone_Number = models.CharField(max_length=11,unique=True)
  phone_Number = models.CharField(max_length=11,unique = True, 
                                  validators=[
                                              # MinLengthValidator(11, message="Phone No. must have 11 numeric characters."),
                                              # int_list_validator(sep = '', message="phone No. is not valid"),
                                              ])
  email = models.EmailField(unique=True)
  address = models.CharField(max_length=255)
  password = models.CharField(max_length=255, validators=[
                                                          # MinLengthValidator(8, message="Password must have at least 8 characters."),
                                                          # MaxLengthValidator(15, message="password must have at most 15 characters."),
                                                          ])
  objects = CustomUserManager()

  groups = models.ManyToManyField(
        Group,
        related_name='barber_groups'
    )
  user_permissions = models.ManyToManyField(
        Permission,
        related_name='barber_user_permissions'
    )

