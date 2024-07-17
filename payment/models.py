from lutos_app.models import Product
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import datetime
# Create your models here.


#create otder model 
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    shipping_adress1 = models.TextField(max_length=15000)
    amout_paid = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered =models.DateTimeField(auto_now_add=True)
    shipped = models.BooleanField(default= False)
    date_shiped =models.DateTimeField(blank=True,null=True)

#auto add shipping date
@receiver(pre_save, sender=Order)
def set_shipeddate_on_update(sender,instance,**kwargs):
    if instance.pk:
        now = datetime.datetime.now()
        obj = sender._default_manager.get(pk=instance.pk)
        if instance.shipped and not obj.shipped:
            instance.date_shiped = now


    def __str__(self):
        return f'Order - {str(self.id)}'

#create otder model items model

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='product_order_items')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_order_items')
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'OrderItem - {str(self.id)}'


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    shipping_full_name = models.CharField(max_length=50)
    shipping_email = models.CharField(max_length=50)
    shipping_adress1 = models.CharField(max_length=50)
    shipping_adress2 = models.CharField(max_length=50,null=True,blank=True)
    shipping_city = models.CharField(max_length=50)
    shipping_state = models.CharField(max_length=50,null=True,blank=True)
    shipping_zip_code = models.CharField(max_length=50,null=True,blank=True)
    shipping_country = models.CharField(max_length=50)


# don't prularlize
class Meta:
    verbose_name_plural = 'ShippingAddress'   

    def __str__(self):
        return f'Shipping Adress - {str(self.id)}'