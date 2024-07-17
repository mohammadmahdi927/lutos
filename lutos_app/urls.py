from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="home"),
    path("login/",views.login_user, name="login"),
    path("logout/",views.logout_user, name="logout"),
    path("signup/", views.signup_user, name="signup"),
    path("product/<int:pk>",views.product,name="product"),
    path("category/<str:cat>",views.category, name="category"),
    path("category_summery/",views.category_summery, name="category_summery"),
    path("update_profile/",views.update_profile, name="update_profile"),
    path("update_info/",views.update_info, name="update_info"),
    path("update_password/",views.update_password, name="update_password"),
    path('search/',views.search, name='search'),
]
