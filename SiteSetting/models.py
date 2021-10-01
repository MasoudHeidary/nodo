from os.path import basename, split
from django.db import models


def home_slider_image_name(instance, filename):
    base_name = basename(filename)
    head, tail = split(base_name)
    return f"HomeSlider/{instance.Title1}.{tail}"


class HomeSliderManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(Active=True)


class HomeSlider(models.Model):
    Title1 = models.CharField(max_length=50)
    Title2 = models.CharField(max_length=50)
    Button = models.CharField(max_length=50)
    Color = models.CharField(max_length=50)
    Image = models.ImageField(upload_to=home_slider_image_name)

    Active = models.BooleanField(default=False)

    objects = HomeSliderManager()
