from django.shortcuts import render,redirect
from django.contrib import messages 

from django.contrib.auth.models import User

from lutos_app.models import Product,Profile
from cart_app.cart import Cart
from payment.forms import ShippingForm,PaymentForm
from payment.models import ShippingAddress,Order,OrderItem

import datetime



# Create your views here.













def orders(request,pk):
    if request.user.is_authenticated and request.user.is_superuser:
        order = Order.objects.get(id = pk)
        items = OrderItem.objects.filter(order = pk)
            
        if request.POST:
            status = request.POST.get('shipping_status')
            if status == "false":
                Order.objects.filter(id=pk).update(shipped=False)
                messages.success(request, "ارسال لغو شد")
            else:

                now = datetime.datetime.now()
                Order.objects.filter(id=pk).update(shipped=True,date_shiped = now)
                messages.success(request, "ارسال شد")
            
        else:
            pass
            
        





        return render (request, 'orders.html',{'order':order,'items':items})

    else:
        messages.success(request, "access denied")
        return redirect('home')



def shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        cart = Cart(request)
        
        orders = Order.objects.filter(shipped = True)
        quantities = cart.get_quants()
        totals = cart.cart_total()

        if request.POST:
            status = request.POST.get('shipping_status')
            num = request.POST['num']
            order = Order.objects.filter(id=num)
            now = datetime.datetime.now()
            order.update(shipped=False,date_shiped = now)
        else:
            pass





        return render (request, 'shipped_dash.html',{'orders':orders, 'quantities':quantities,'totals':totals,})
    else:

    
        messages.success(request, "access denied")
        return redirect('home')



def not_shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.filter(shipped = False)
        if request.POST:
            status = request.POST.get('shipping_status')
            num = request.POST['num']
            order = Order.objects.filter(id=num)
            now = datetime.datetime.now()
            order.update(shipped=True,date_shiped = now)
        else:
            pass

        return render (request, 'not_shipped_dash.html',{'orders':orders})
    else:

    
        messages.success(request, "access denied")
        return redirect('home')



def process_order(request):
    if request.POST:
        #get the cart
        cart = Cart(request)
        quantities = cart.get_quants()
        cart_products = cart.get_prods()
        totals = cart.cart_total()
        # get billing form from the last page
        payment_form = PaymentForm(request.POST or None)

        # get shipping session data
        my_shipping = request.session.get('my_shipping')

        #gather oreder info 
        
        full_name = my_shipping['shipping_full_name']
        email= my_shipping['shipping_email']
        
        # create shipping adress from session info
        shipping_adress = f"{my_shipping['shipping_adress1']}\n{my_shipping['shipping_adress2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zip_code']}\n"
        amout_paid= totals
        
        #creat an order

        if request.user.is_authenticated:
            user = request.user
            order = Order(user=user, full_name=full_name, email=email, shipping_adress1=shipping_adress, amout_paid=amout_paid)

            order.save()
            
        
            # add order items

            # get order id
            order_id = order.id
            # get product info
            for product in cart_products:
                product_id = product.id
                # get product price
                if product.Sale == True:
                    price = product.Discount
                else:
                    price = product.Price
                
                for key,value in quantities.items():
                    if int(key) == product.id :
                        #create order item
                        creat_order_item = OrderItem(order_id=order_id, product_id=product_id, price=price, quantity=value, user=user)
                        creat_order_item.save()

                #delete our cart
                for key in list(request.session.keys()):
                    if key == "session_key":
                        del request.session[key]


            current_user = Profile.objects.filter(user__id=request.user.id)

            current_user.update(old_cart="")

                

            messages.success(request, 'order placed')
            return redirect('home')
        else:
            user = request.user
            order = Order( full_name=full_name, email=email, shipping_adress1=shipping_adress, amout_paid=amout_paid)
            order.save()
            


            order_id = order.id
            # get product info
            for product in cart_products:
                product_id = product.id
                # get product price
                if product.Sale == True:
                    price = product.Discount
                else:
                    price = product.Price
                
                for key,value in quantities.items():
                    if int(key) == product.id :
                        #create order item
                        creat_order_item = OrderItem(order_id=order_id, product_id=product_id, price=price, quantity=value)
                        creat_order_item.save()


                #delete our cart
                for key in list(request.session.keys()):
                    if key == "session_key":
                        del request.session[key]




            
            messages.success(request,'order placed')
            return redirect('login')

    
    else:
        messages.success(request, 'اول وارد حساب خود شوید')
        return redirect('home')
    

def billibg_info(request):
    if request.POST:

        cart = Cart(request)
        quantities = cart.get_quants()
        cart_products = cart.get_prods()
        totals = cart.cart_total()

        #create session with shipping info

        my_shipping = request.POST
        request.session['my_shipping'] = my_shipping
    
        # check for loged in user
        if request.user.is_authenticated:
            billibg_form = PaymentForm()
            
            
            return render(request,'billibg_info.html',{
                        'cart_products': cart_products,
                        'quantities':quantities,
                        'total':totals,
                        'shipping_info':request.POST,
                        'billibg_form':billibg_form,
                    })
    


        else:
            billibg_form = PaymentForm()

            return render(request,'billibg_info.html',{
                        'cart_products': cart_products,
                        'quantities':quantities,
                        'total':totals,
                        'shipping_info':request.POST,
                        'billibg_form':billibg_form,

                    })


    else:
        messages.success(request, 'اول وارد حساب خود شوید')
        return redirect('home')

def payment_success(request):
    return render(request, 'payment.html')

def checkout(request):
    cart = Cart(request)
    quantities = cart.get_quants()
    cart_products = cart.get_prods()
    totals = cart.cart_total()

    if request.user.is_authenticated:
         shipping_user = ShippingAddress.objects.filter(user__id=request.user.id).first()
         shipping_Form = ShippingForm(request.POST or None, instance= shipping_user)
         return render(request,'checkout.html',{
        'cart_products': cart_products,
        'quantities':quantities,
        'total':totals,
        'shipping':shipping_Form,

    })
    else:

        shipping_Form = ShippingForm(request.POST or None)
        return render(request,'checkout.html',{
            'cart_products': cart_products,
            'quantities':quantities,
            'total':totals,
            'shipping':shipping_Form,
        })
    