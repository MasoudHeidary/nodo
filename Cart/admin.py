from django.contrib import admin

from .models import Cart, CartItems, ShippingAddress


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['to_user', 'IsPaid', 'PaymentDate']

    @admin.display(description="to user")
    def to_user(self, obj: Cart):
        return obj.ToUser.username


@admin.register(CartItems)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['to_cart', 'to_sub_product', 'Price', 'Count']

    @admin.display(description='to cart')
    def to_cart(self, obj: CartItems):
        return obj.ToCart

    @admin.display(description='to sub product')
    def to_sub_product(self, obj: CartItems):
        return obj.ToSubProduct


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['to_cart', 'State', 'City']

    @admin.display(description="to cart")
    def to_cart(self, obj: ShippingAddress):
        return obj.ToCart
