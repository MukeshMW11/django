from django.db import models
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    descriptipn = models.TextField()
    price  = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)


class Customer():
    MEMBERSHIP_BRONZE= 'B'
    MEMBERSHIP_SILVER= 'S'
    MEMBERSHIP_GOLD= 'G'
    MEMBERSHIP_PLATINUM= 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
        (MEMBERSHIP_PLATINUM, 'Platinum'),
    ]
    first_name = models.CharField(max_length=50)    
    last_name = models.CharField(max_length=50)    
    email = models.EmailField(max_length=200,unique=True) 
    phone = models.CharField(max_length=15)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES, default =MEMBERSHIP_BRONZE)



class Order(models.Model):

    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETED = 'C'
    PAYMENT_FAILED = 'F'

    PAYMENT_CHOICES = [

    (PAYMENT_PENDING, 'Pending'),
    (PAYMENT_COMPLETED, 'Completed'),
    (PAYMENT_FAILED, 'Failed'), 

    ]

    placed_at = models.CharField(default=timezone.now)    
    payment_status = models.CharField(choices=)