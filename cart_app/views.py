from django.shortcuts import render,get_object_or_404
from .cart import Cart
from lutos_app.models import Product
from django.http import JsonResponse,HttpResponseBadRequest
from django.contrib import messages

# Create your views here.


def cart_summery(request):
    cart = Cart(request)
    quantities = cart.get_quants()
    cart_products = cart.get_prods()
    totals = cart.cart_total()
    return render(request,'cart_summery.html',{
        'cart_products': cart_products,
        'quantities':quantities,
        'total':totals,

    })




def cart_add(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('Invalid request')

    product_id = int(request.POST['product_id'])
    product_qty = int(request.POST['product_qty'])

    product = get_object_or_404(Product, id=product_id)
    cart_quantity = Cart(request).add(product, product_qty)
    messages.success(request,message='به سبد خرید اضافه شد')

    return JsonResponse({
        'product_price': str(product.Price),  
        'product_name': str(product.Name),   
        'qty': str(cart_quantity),   
        'ID': str(product.id),   
    })




def cart_update(request):
    cart = Cart(request)

    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        
        
        cart.update(product=product_id,quantity=product_qty)

        response_data = {
            'qty':product_qty,
        }

        return JsonResponse(response_data)
    else:
        # Handle invalid requests (e.g., not a POST request)
        return HttpResponseBadRequest('Invalid request')


def cart_delete(request):
    cart = Cart(request)

    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))
        
        cart.delete(product=product_id)

        return JsonResponse({'product':product_id})
    else:
        return HttpResponseBadRequest('Invalid request')
    
def update_user(request):
    return render(request,'update_user.html',{
        
    })