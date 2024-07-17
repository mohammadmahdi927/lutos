from django import forms
from .models import ShippingAddress


class PaymentForm(forms.Form):
   
    cart_number =forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'شماره کارت'}),required=True)
    cart_expire =forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'تاریخ انقضا'}),required=True)
    cart_cvv2 =forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'cvv2'}),required=True)
    cart_password =forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'رمز'}),required=True)
    cart_shaba =forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'شماره شبا'}),required=False)

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'نام خود را وارد کنید '}),required=True)
    shipping_email = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'آدرس خودایمیل را وارد کنید '}),required=True)
    shipping_adress1 = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'آدرس خود را وارد کنید '}),required=True)
    shipping_adress2 = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'آدرس خود را وارد کنید '}),required=False)
    shipping_city = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'شهر خود را وارد کنید '}),required=True)
    shipping_state = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'استان خود را وارد کنید '}),required=False)
    shipping_zip_code = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'کد پستی خود را وارد کنید '}),required=False)
    shipping_country = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'کشور خود را وارد کنید '}),required=True)


    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_adress1', 'shipping_adress2', 'shipping_city', 'shipping_state', 'shipping_zip_code','shipping_country']

        exclude = ['user',]

    