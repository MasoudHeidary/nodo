from django.contrib import admin

from .models import ShopAccount


@admin.register(ShopAccount)
class ShopAccountAdmin(admin.ModelAdmin):
    list_display = ['Name']
