from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
import json

from payment.forms import ShippingForm
from payment.models import ShippingAddress

from .forms import SignUpForm,UpdateUserForm,ChangePasswordForm,UserInfoForm
from cart_app.cart import Cart
#imort UpdateProfileForm 


# Create your views here.

def search(request):
# check if they fiiled the form
    if request.method == 'POST':
        searched  =request.POST['search']
        # Query the database for Product model
        searched = Product.objects.filter(Name__icontains=searched)
        # test for null
        if not searched:
            messages.success(request,"محصولی با این نام یافت نشد")
            return render(request, 'search.html')
        else:
            return render(request, 'search.html', {'searched':searched})
    else:
        return render(request, 'search.html', {})

def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)

        shipping_user = ShippingAddress.objects.filter(user__id=request.user.id).first()


        form = UserInfoForm(request.POST or None, instance= current_user)

        shipping_Form = ShippingForm(request.POST or None, instance= shipping_user)

        if form.is_valid() or shipping_Form.is_valid():
            form.save()
            shipping_Form.save()
            messages.success(request,"پروفایل شما با موفقیت بروزرسانی شد")
            return redirect('home')
        else:
            for error in form.errors:
                messages.error(request, form.errors[error])
            return render(request, 'update_info.html', {'form':form,'shipping':shipping_Form})
    else:
        messages.success(request, 'Please login first')
        return redirect('login')
    
def index(request):

    all_p = Product.objects.all()
    return render(request, "index.html",{
        'product':all_p,
        
    })

def login_user(request):
     

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # do some shoping cart stuff here
            current_user = Profile.objects.get(user__id=request.user.id)
            # get their cart
            saved_cart = current_user.old_cart
            # convert back string to python dic
            if saved_cart:
                # convert back string to python dic using JSON
                converted_cart = json.loads(saved_cart)
                # add loaded dic to session
                cart =Cart(request)
                # loop on cart and add to database
                for key,value in converted_cart.items():
                    cart.db_add(product=key,quantity=value)





            return redirect('home')
        else:
            messages.success(request, ("نام کاربری یا رمز عبور اشتباه است"))
            return render(request, "login.html")
    else:
        return render(request, "login.html")
     





    
def update_profile(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = UpdateUserForm(request.POST or None, instance= current_user)
        if form.is_valid():

            form.save()

            login(request, current_user)

            return redirect('home')
        else:
            for error in form.errors:
                messages.error(request, form.errors[error])
            return render(request, 'update_profile.html', {'form':form})
        
    else:
        messages.success(request, 'Please login first')
        return redirect('login')

def logout_user(request):
    logout(request)
    messages.success(request,message='از اکانت خود خارج شدید')
    return redirect('home')

    # Save user data after successful registration

# sign up user
def signup_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'ثبت نام با موفقیت انجام شد لطفااطلاعات خود را تکمیل کنید')
            return redirect('update_info')
    return render(request, 'signup.html', {'form': form})

def product(request,pk):
    product = Product.objects.get(id=pk)
    
    return render(request,'product.html',{
        'product':product,
        
    })

def category(request,cat):
    #capitalized_cat = string.capwords(cat)
    cat = cat.replace(" ","-")
    try:
        category = Category.objects.get(Name=cat)
        product = Product.objects.filter(Category = category)
        return render(request,'category.html',{
            'category':category,
            'product':product,
        })
    except:
        messages.success(request,"دسته بندی وجود نداشت")
        return redirect('home')
    
def category_summery(request):
    
    categories = Category.objects.all()
        

    return render(request,'category_summery.html',{
            'categories':categories,
            
        })

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        #did they fill the form 
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your password was successfully updated!')
                login(request,current_user )
                return redirect('home')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('update_password')


        else:
            form = ChangePasswordForm(current_user)
            return render(request, 'update_password.html', {'form':form})
        
        
        
    else:
        # if user is not authenticated, redirect to login page
        messages.warning(request, 'Please login first')
        return redirect('login')