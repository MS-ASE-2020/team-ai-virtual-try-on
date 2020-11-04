from django.db import models
from django.contrib.auth.models import AbstractUser


def user_directory_path(instance, filename):
    if instance.is_saler:
        return 'salers/saler_{}/{}'.format(instance.name, filename)
    return 'customers/customer_{}/{}'.format(instance.name, filename)


def product_directory_path(instance, filename):
    return 'products/{}/{}'.format(instance.name, filename)


class MyUser(AbstractUser):
    username = None
    name = models.CharField('name', max_length=20, primary_key=True)
    phone_number = models.DecimalField('phone_number', max_digits=11, decimal_places=0, blank=False)
    is_saler = models.BooleanField(default=False)
    self_pics = models.ImageField('self_pics', upload_to=user_directory_path)
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['phone_number', 'is_saler']

    class Meta:
        db_table = 'MyUser'
    
    def __str__(self):
        return self.name
        

class Product(models.Model):
    name = models.CharField('name', max_length=20, blank=False)
    price = models.FloatField('price', default=0.0, blank=False)
    link = models.URLField('link', max_length=255, default="https://www.taobao.com")
    overall_score = models.FloatField('overall_score', default=0)
    number_people_scoring = models.DecimalField('number_people_scoring', max_digits=10, decimal_places=0, default=0)
    owned_saler = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    pics = models.ImageField('pics', upload_to=product_directory_path)

    class Meta:
        db_table = 'Product'
