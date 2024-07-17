from django.urls import path
from . import views

urlpatterns = [
    path("",views.cart_summery, name="cart_summery"),
    path("add/",views.cart_add, name="cart_add"),
    path("update/",views.cart_update, name="update"),
    path("delete/",views.cart_delete, name="delete"),
]
