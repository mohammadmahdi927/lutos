from django.db import models
import datetime 
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.



# customer profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=15, blank=True)
    adress1 = models.CharField(max_length=200, blank=True)
    adress2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zip_code = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    old_cart = models.TextField(default='{}', null=True, blank=True)

    def __str__(self):
        return self.user.username
    
# user profile by default when user signsup
def Create_profile(sender, instance, created, **kwards):
    if created:
        user_profile = Profile.objects.create(user=instance)
        user_profile.save()

# automate the profile creation
post_save.connect(Create_profile, sender=User)









class Category(models.Model):
    Name = models.CharField(("Ctegory name"),max_length=255,)
    # description = models.CharField(max_length=512)
    
    def __str__(self):
        return self.Name

class Customer(models.Model):
    Name = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=15)
    Address = models.CharField(max_length=512)
    Email = models.EmailField(max_length=128)
    Password = models.CharField( max_length=50)

    def __str__(self):
        return f'{self.Name},{self.LastName},{self.PhoneNumber},{self.Address},{self.Email},{self.Password}'
    
class Product(models.Model):
    Name = models.CharField(max_length=50,)
    Description = models.CharField(max_length=1024, null = False ,blank=True,default='')
    Category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    Price = models.DecimalField(max_digits=15,default =0,decimal_places=0)
    Image = models.ImageField(upload_to="upload/product")
    Image1 = models.ImageField(upload_to="upload/product")
    Image2 = models.ImageField(upload_to="upload/product")
    Image3 = models.ImageField(upload_to="upload/product")
    Stars = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    Sale = models.BooleanField(default=False)
    Discount = models.DecimalField(max_digits=15,default =0,decimal_places=0)

    Featured = models.BooleanField(default=False)
    
    Slide = models.BooleanField(default=False)
    Active = models.BooleanField(default=False)
    Title = models.CharField(max_length=255,null=True,blank=True)


    def __str__(self):
        return f'{self.Name},{self.Description},{self.Category},{self.Price},{self.Image},{self.Stars},{self.Sale},{self.Discount},{self.Image},{self.Image1},{self.Image2},{self.Image3},{self.Featured}{self.Active},{self.Title}{self.Slide}'
    
class Order(models.Model):
    OrderNumber = models.DecimalField(default =0,decimal_places=0,max_digits=1200)
    Item = models.ForeignKey(Product, verbose_name=(""), on_delete=models.CASCADE)
    Address = models.CharField(max_length=500)
    date = models.DateField(default=datetime.datetime.today)
    Status = models.BooleanField(("Status"),default=False)
    def __str__(self):
        return f'{self.OrderNumber},{self.Item},{self.Address},{self.date},{self.Status}'


    
