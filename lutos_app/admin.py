from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Profile)


# mix profile info and user info
class ProfileInline(admin.StackedInline):
    model  = Profile

# extends user model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ['first_name', 'last_name', 'email', 'username']
    inlines = [ProfileInline]


# unregister user model
admin.site.unregister(User)

#re-register user model
admin.site.register(User, UserAdmin)