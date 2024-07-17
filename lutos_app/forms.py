from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile





class UserInfoForm(forms.ModelForm):
    phone = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'شماره تلفن خود را وارد کنید '}),required=False)
    adress1 = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'آدرس خود را وارد کنید '}),required=False)
    adress2 = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'آدرس خود را وارد کنید '}),required=False)
    city = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'شهر خود را وارد کنید '}),required=False)
    state = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'استان خود را وارد کنید '}),required=False)
    zip_code = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'کد پستی خود را وارد کنید '}),required=False)
    country = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'کشور خود را وارد کنید '}),required=False)

    class Meta:
        model = Profile
        fields = ['phone', 'adress1', 'adress2', 'city', 'state', 'zip_code','country']

class ChangePasswordForm(SetPasswordForm):
        new_password1 = forms.CharField(
        label="",
        max_length=255,
        widget= forms.PasswordInput(attrs={
            'class':'form-control ',
            'name':'password',
            'type':'password',
            'placeholder':'رمز خود را وارد کنید'
            }
        )
    )
        new_password2 = forms.CharField(
        label="",
        max_length=255,
        widget= forms.PasswordInput(attrs={
            'class':'form-control ',
            'name':'password',
            'type':'password',
            'placeholder':'رمز خود مجدد را وارد کنید'
            }
        )
    )
        class Meta:
            model = User
            fields = ['new_password1', 'new_password2']

class UpdateUserForm(UserChangeForm):
    password = None

    first_name = forms.CharField(
        label="",
        max_length=255,
        widget= forms.TextInput(attrs={'class':'form-control ','placeholder':'نام خود را وارد کنید ',})
    )
    last_name = forms.CharField(
        label="",
        max_length=255,
        widget= forms.TextInput(attrs={'class':'form-control ','placeholder':'نام خانوادگی خود را وارد کنید'})
    )
    email = forms.EmailField(
        label="",
        max_length=255,
        widget= forms.TextInput(attrs={'class':'form-control ','placeholder':'ایمیل خود را وارد کنید'})
    )
    username = forms.CharField(
        label="",
        max_length=255,
        widget= forms.TextInput(attrs={'class':'form-control ','placeholder':'نام کاربری خود را وارد کنید '})
    )
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=155,
        widget= forms.TextInput(attrs={'class':'form-control ','placeholder':'نام خود را وارد کنید ',}),
        error_messages={'required': 'نام را وارد کنید'})
    
    last_name = forms.CharField(max_length=155,
        widget= forms.TextInput(attrs={'class':'form-control ','placeholder':'نام خانوادگی خود را وارد کنید ',}),
        error_messages={'required': 'نام خانوادگی را وارد کنید'})
    
    username = forms.CharField(max_length=155,
        widget= forms.TextInput(attrs={'class':'form-control ','placeholder':'نام مستعار خود را وارد کنید ',}),
        error_messages={'required': 'نام مستعار را وارد کنید'})
    
    email = forms.EmailField(max_length=155,
        widget= forms.TextInput(attrs={'class':'form-control ','placeholder':'ایمیل خود را وارد کنید ',}),
        error_messages={'required': 'ایمیل را وارد کنید'})
    
    password1 = forms.CharField(
         label="",
         max_length=255,
         widget= forms.PasswordInput(attrs={
             'class':'form-control ',
             'name':'password',
             'type':'password',
             'placeholder':'رمز خود را وارد کنید'
             }
         ),
         error_messages={'required': 'رمز را وارد کنید'})
    
    password2 = forms.CharField(
         label="",
         max_length=255,
         widget= forms.PasswordInput(attrs={
             'class':'form-control ',
             'name':'password',
             'type':'password',
             'placeholder':'رمز خود را مجددا وارد کنید'
             }
         ),
         error_messages={'required': 'رمز را مجددا وارد کنید'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("رمز های وارد شده مطابقت ندارند")
        return password2
        
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("نام مستعار وارد شده موجود است")
        
    def clean_email(self):
        email = self.cleaned_data["email"]
        if not email:
            raise forms.ValidationError("ایمیل را وارد کنید")
        return email