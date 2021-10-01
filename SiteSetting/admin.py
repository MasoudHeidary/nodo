from django.contrib import admin

from .models import HomeSlider


@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ['Title1', 'Title2', 'Button', 'Image', 'Active']
    list_editable = ['Active']
