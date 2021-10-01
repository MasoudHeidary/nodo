from django.urls import path

from . import views

app_name = "Cart"
urlpatterns = [
    path('cart/', views.cart_page, name="Cart"),
    path('cart/add/<int:sub_product_id>/<int:count>/', views.add_to_cart, name="Add"),
    path('cart/inc/<int:sub_product_id>/<int:count>/', views.cart_page_increase_count, name="Increase"),
    path('cart/dec/<int:sub_product_id>/<int:count>/', views.cart_page_decrease_count, name="Decrease"),
    path('cart/receipt/', views.cart_receipt_page, name="Receipt"),
    path('cart/pay/', views.cart_pay, name="Pay"),
    path('old-cart/', views.OldCartListView.as_view(), name="OldCartList"),
    path('old-cart/<int:pk>/', views.OldCartDetailView.as_view(), name="OldCartDetail"),
]
