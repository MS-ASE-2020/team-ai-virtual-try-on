from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

def user_directory_path(instance, filename):
    if instance.is_saler:
        return 'salers/saler_{}/img/{}'.format(instance.name, filename)
    return 'customers/customer_{}/img/{}'.format(instance.name, filename)


def product_directory_path(instance, filename):
    return 'products/{}/img/{}'.format(instance.id, filename)


class MyUser(AbstractUser):
    username = None
    name = models.CharField('name', max_length=20, primary_key=True)
    phone_number = models.CharField('phone_number', max_length=11, blank=False)
    is_saler = models.BooleanField(default=False)
    self_pics = models.ImageField('self_pics', upload_to=user_directory_path)
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['phone_number', 'is_saler']

    class Meta:
        db_table = 'MyUser'
    
    def __str__(self):
        return self.name
        

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('name', max_length=20, blank=False)
    price = models.FloatField('price', default=0.0, blank=False)
    link = models.URLField('link', max_length=255, default="https://www.taobao.com")
    number_people_scoring_one = models.IntegerField('number_people_scoring_one', default=0)
    number_people_scoring_two = models.IntegerField('number_people_scoring_two', default=0)
    number_people_scoring_three = models.IntegerField('number_people_scoring_three', default=0)
    number_people_scoring_four = models.IntegerField('number_people_scoring_four', default=0)
    number_people_scoring_five = models.IntegerField('number_people_scoring_five', default=0)
    owned_saler = models.ForeignKey(MyUser, on_delete=models.CASCADE, limit_choices_to={'is_saler': True})
    pics = models.ImageField('pics', upload_to=product_directory_path)

    class Meta:
        db_table = 'Product'
