from django.shortcuts import render

from SiteSetting.models import HomeSlider


def home_page(request):
    home_slider_slides = HomeSlider.objects.active()

    context = {
        'HomeSlider': home_slider_slides
    }

    return render(request, 'Root/Home.html', context)
