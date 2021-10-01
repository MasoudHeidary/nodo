from django.urls import path

from . import views

app_name = "ShopAdmin"
urlpatterns = [
    path('shop-admin/', views.admin_dashboard, name='Dashboard'),
    path('shop-admin/products/', views.AdminProductListView.as_view(), name="Product"),
    path('shop-admin/add-sub-product/<int:id>', views.admin_add_sub_product, name="AddSubProduct"),
    path('shop-admin/add-product/', views.admin_add_product, name="AddProduct"),
]
