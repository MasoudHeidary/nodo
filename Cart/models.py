from django.db import models
from django.utils import timezone
from persiantools.digits import en_to_fa
from persiantools.jdatetime import JalaliDateTime
from django.contrib.humanize.templatetags.humanize import intcomma

from Product.models import SubProduct
from Account.models import CustomUser


class Cart(models.Model):
    IsPaid = models.BooleanField(default=False)
    PaymentDate = models.DateTimeField(null=True, blank=True)

    ToUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.ToUser.username

    def total(self):
        items: [CartItems] = self.cartitems_set.all()
        total_price = 0
        for i in items:
            total_price += i.item_price()
        return total_price

    def template_total(self):
        return en_to_fa(intcomma(self.total()))

    def total_plus_shipping(self):
        return self.total() + 20_000

    def template_total_plus_shipping(self):
        # return f"{en_to_fa(intcomma(self.total()))} + {en_to_fa(intcomma(20_000))}" + \
        #        f" = {en_to_fa(intcomma(self.total_plus_shipping()))}" + 'ت'
        return f"{en_to_fa(intcomma(self.total_plus_shipping()))}" + 'ت'

    def template_date_time(self):
        if self.PaymentDate:
            return en_to_fa(JalaliDateTime(
                timezone.localtime(self.PaymentDate)
            ).strftime("%Y/%m/%d %H:%M"))
        return False


class CartItems(models.Model):
    ToCart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    ToSubProduct = models.ForeignKey(SubProduct, on_delete=models.CASCADE)
    Price = models.IntegerField()
    Count = models.IntegerField()

    def __str__(self):
        return self.ToCart.__str__()

    def item_price(self):
        return self.Price * self.Count

    def template_item_price(self):
        return en_to_fa(intcomma(self.item_price()))


class ShippingAddress(models.Model):
    State = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    Address = models.CharField(max_length=250)
    HouseNumber = models.CharField(max_length=5)
    FloorNumber = models.CharField(max_length=3)
    ZipCode = models.CharField(max_length=10)

    ToCart = models.OneToOneField(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return self.ToCart.__str__()
