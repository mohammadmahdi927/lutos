from lutos_app.models import Product,Profile
from django.db.models import Q
from django.contrib import messages

import decimal

class Cart:
    def __init__(self, request):
        self.session = request.session
        # get request
        self.request = request
        # Initialize the cart as an empty dictionary
        self.cart = self.session.get('session_key', {})
        if 'session_key' not in request.session:
            self.cart = self.session['session_key'] = {}

        # No need to reassign self.cart here; it's already set correctly



    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)     

        if product_id not in self.cart:
            self.cart[product_id] = int(product_qty)
            # Mark the session as modified
        self.session.modified = True

        # deal with loged in users
        if self.request.user.is_authenticated:
            #get the current user profile
            current_user = Profile.objects.filter(Q(user__id=self.request.user.id))
            # convert {'1':2} to {"1":2}
            carty = str(self.cart)
            carty = carty.replace("'","\"")
            # save carty to Profile model
            current_user.update(old_cart=str(carty))

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id not in self.cart:
          
            self.cart[product_id] = int(product_qty)
            # Mark the session as modified
        self.session.modified = True
        # deal with loged in users
        if self.request.user.is_authenticated:
            #get the current user profile
            current_user = Profile.objects.filter(Q(user__id=self.request.user.id))
            # convert {'1':2} to {"1":2}
            carty = str(self.cart)
            carty = carty.replace("'","\"")
            # save carty to Profile model
            current_user.update(old_cart=str(carty))
    def __len__(self):
        return len(self.cart)

    def get_quants(self):
        quantities = self.cart
        return quantities


    def get_prods(self):
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        return products

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)
             
        ourcart = self.cart
        ourcart[product_id] = product_qty
        self.session.modified =True

          # deal with loged in users
        if self.request.user.is_authenticated:
            #get the current user profile
            current_user = Profile.objects.filter(Q(user__id=self.request.user.id))
            # convert {'1':2} to {"1":2}
            carty = str(self.cart)
            carty = carty.replace("'","\"")
            # save carty to Profile model
            current_user.update(old_cart=str(carty))

        thing = self.cart
        return thing



    def delete(self,product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]
            
        self.session.modified = True

  # deal with loged in users
        if self.request.user.is_authenticated:
            #get the current user profile
            current_user = Profile.objects.filter(Q(user__id=self.request.user.id))
            # convert {'1':2} to {"1":2}
            carty = str(self.cart)
            carty = carty.replace("'","\"")
            # save carty to Profile model
            current_user.update(old_cart=str(carty))







    def cart_total(self):
        product_ids = self.cart.keys()
        
        products = Product.objects.filter(id__in=product_ids)
        
        quantities = self.cart
        total =0 
        for key, value in quantities.items():
            key = int(key)
            value = int(value)
            for product in products:
                if product.id == key:
                    if product.Sale == True:
                        total += (product.Discount * value)
                    else:
                        total += (product.Price * value) # Use product.Price instead of Product.Price
    
        return total

