from django.urls import path

from . import views

app_name = "Product"
urlpatterns = [
    path('books/', views.ProductListView.as_view(), name='ProductList'),
    path('books/<category>/', views.ProductListView.as_view(), name='ProductListWithCategory'),
    path('book/<slug>/', views.ProductDetailView.as_view(), name='ProductDetail'),
]
