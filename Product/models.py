from random import randint

from django.contrib.humanize.templatetags.humanize import intcomma
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from persiantools.digits import en_to_fa

from ShopAccount.models import ShopAccount
from utils.file import get_file_name_ext


class ProductCategory(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


def product_image_name(instance, filename):
    head, tail = get_file_name_ext(filename)
    return f"Product/{instance.Slug}.jpg"


class ProductManager(models.Manager):
    def available(self):
        return self.get_queryset().filter(subproduct__Number__gt=0).distinct()


class Product(models.Model):
    Name = models.CharField(max_length=250)
    Writer = models.CharField(max_length=150)
    Translator = models.CharField(max_length=150, null=True, blank=True)
    Publisher = models.CharField(max_length=150)
    Description = models.TextField()
    OneLineDescription = models.CharField(max_length=150, null=True, blank=True)
    Barcode = models.CharField(max_length=100)
    Active = models.BooleanField(default=False)

    ToCategory = models.ManyToManyField(ProductCategory, null=True, blank=True)

    Slug = models.SlugField(allow_unicode=True, blank=True, max_length=100, unique=True)
    Image = models.ImageField(upload_to=product_image_name, null=True)

    objects = ProductManager()

    def __str__(self):
        return self.Publisher + self.Name

    def get_price_list_with_number(self):
        sub_product_list = self.subproduct_set.all()
        return [(i.Price, i.Number) for i in sub_product_list]

    def min_max_price(self):
        price_list = [i[0] for i in self.get_price_list_with_number()]
        if not price_list:
            return None
        return min(price_list), max(price_list)

    def template_min_max_price(self):
        min_price, max_price = self.min_max_price() or (None, None)
        if not min_price:
            return None
        if min_price == max_price:
            message = f"{en_to_fa(intcomma(min_price))}" \
                      f" ت"
        else:
            message = f" از" \
                      f"{en_to_fa(intcomma(min_price))}" \
                      f" ت تا " \
                      f"{en_to_fa(intcomma(max_price))}" \
                      f" ت"
        return message

    def is_available(self):
        if self.subproduct_set.filter(Number__gt=0).exists():
            return True
        return False

    def have_second_hand(self):
        if self.subproduct_set.filter(IsSecondHand=True, Number__gt=0).exists():
            return True
        return False

    def have_new(self):
        if self.subproduct_set.filter(IsSecondHand=True, Number__gt=0).count() != self.subproduct_set.filter(
                Number__gt=0).count():
            return True
        return False


@receiver(pre_save, sender=Product)
def product_slug_generator(sender: Product, instance: Product, **kwargs):
    if instance.Slug:
        return instance.Slug.replace(' ', '-')
    slug = f"{instance.Publisher}-{instance.Name}".replace(' ', '-')

    slug_with_random_number = slug
    while sender.objects.filter(Slug=slug_with_random_number).exists():
        slug_with_random_number = slug + f"{randint(0, 1_000)}"

    instance.Slug = slug_with_random_number


class SubProduct(models.Model):
    IsSecondHand = models.BooleanField(default=False)
    second_hand_rate = (
        ('N', 'N'),
        ('A+', 'A+'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )
    SecondHandRate = models.CharField(max_length=2, choices=second_hand_rate)

    Price = models.IntegerField()
    Number = models.SmallIntegerField()
    BriefDescription = models.CharField(max_length=50, default=" ")

    ToShop = models.ForeignKey(ShopAccount, on_delete=models.CASCADE)
    ToProduct = models.ForeignKey(Product, on_delete=models.CASCADE)

    SellOnline = models.BooleanField(default=True)

    def __str__(self):
        return self.ToProduct.Name + " " + self.ToShop.Name
