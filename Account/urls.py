from django.urls import path

from . import views

app_name = "Account"
urlpatterns = [
    path('login/', views.login_take_password, name="LoginTakePassword"),
    path('login/phone-number/', views.login_take_phone_number, name='LoginTakePhoneNumber'),
    path('logout/', views.logout_page, name='Logout'),
]
