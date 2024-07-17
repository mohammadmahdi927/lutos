from django.contrib import admin
from .models import *

from django.contrib.auth.models import User

# Register your models here.
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)

#create order item inline
class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra =0


#extend order model
class OrederAdmin(admin.ModelAdmin):
    model = Order





    readonly_fields = ['date_ordered']
    fields = ["user","full_name","email","shipping_adress1","amout_paid","date_ordered","shipped","date_shiped"]
    inlines = [OrderItemInline]

#unregister order model
admin.site.unregister(Order)
# re-register Oreder and OrderAdmin
admin.site.register(Order, OrederAdmin)
