from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        return self.email



class Products(models.Model):
    name=models.CharField(max_length=1000)
    description= models.CharField(max_length=1000)
    isInStock=models.BooleanField(default=True)
    gender=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    rating=models.IntegerField()
    totalReviewCount=models.IntegerField()
    productionDate=models.DateTimeField(auto_now_add=True)
    price=models.IntegerField()
    brandName=models.CharField(max_length=200)
    productCode=models.IntegerField()
    imageUrl=models.CharField(max_length=200)
    imageone=models.CharField(max_length=200)
    imagetwo=models.CharField(max_length=200)
    imagethree=models.CharField(max_length=200)
    imagefour=models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Reviews(models.Model):
    username=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    userImage=models.FilePathField()
    location=models.CharField(max_length=200)
    rating=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    reviewTitle=models.CharField(max_length=200)
    reviewText=models.CharField(max_length=200)

    def __str__(self):
        return self.name



