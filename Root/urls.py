from django.urls import path

from . import views

app_name = "Root"
urlpatterns = [
    path('', views.home_page, name='Home'),
]
