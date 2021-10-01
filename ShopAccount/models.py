from django.db import models


def shop_image_name(instance, filename):
    return f"{instance.Name}-{filename}"


class ShopAccount(models.Model):
    Name = models.CharField(max_length=150)
    Address = models.CharField(max_length=150)
    Contact = models.CharField(max_length=250)
    Image = models.ImageField(upload_to=shop_image_name)

    def __str__(self):
        return self.Name
