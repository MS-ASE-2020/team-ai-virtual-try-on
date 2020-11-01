from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


def user_directory_path(instance, filename):
    if instance.is_saler:
        return './pics/saler_{}/{}'.format(instance.username, filename)
    return './pics/customer_{}/{}'.format(instance.username, filename)


class Customer(models.Model):
    username = models.CharField('username', max_length=20, primary_key=True)
    password = models.CharField('password', max_length=20, blank=False)
    phone_number = models.DecimalField('phone_number', max_digits=11, decimal_places=0, blank=False)
    self_pics = models.ImageField('self_pics', upload_to=user_directory_path)

    class Meta:
        db_table = 'Customer'


class MyUser(AbstractUser):
    phone_number = models.DecimalField('phone_number', max_digits=11, decimal_places=0, blank=False)
    is_saler = models.BooleanField(default=False)
    self_pics = models.ImageField('self_pics', upload_to=user_directory_path)
    REQUIRED_FIELDS = ['phone_number', 'is_saler']

    class Meta:
        db_table = 'MyUser'
    
    def __str__(self):
        return self.username
        

class Product(models.Model):
    ID = models.CharField('ID', max_length=20, auto_created=True, primary_key=True)
    name = models.CharField('name', max_length=20, blank=False)
    price = models.FloatField('price', default=0.0, blank=False)
    link = models.URLField('link', max_length=255, default="https://www.taobao.com")
    overall_score = models.FloatField('overall_score', default=0)
    number_people_scoring = models.DecimalField('number_people_scoring', max_digits=10, decimal_places=0, default=0)
    owned_saler = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Product'
