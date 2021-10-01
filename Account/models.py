from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models.signals import pre_save
from django.utils import timezone

from utils.Random import random_number
from ShopAccount.models import ShopAccount

from .apps import OneTimePasswordValidTimeSeconds


class CustomUserManager(UserManager):
    def get_user_with_one_time_password(self, phone_number, password):
        q = self.get_queryset().filter(PhoneNumber=phone_number, SMSCode=password)
        if q.exists():
            return q.first()
        return None

    # return SMS code
    def create_one_time_password(self, phone_number):
        user = self.get_queryset().filter(PhoneNumber=phone_number)
        if not user.exists():
            return None

        user: CustomUser = user.first()
        return user.create_sms_code()


class CustomUser(AbstractUser):
    PhoneNumber = models.CharField(max_length=20)
    SMSCode = models.CharField(max_length=6, null=True, blank=True)
    SMSCreatedTime = models.DateTimeField(default=timezone.now())

    ToShopAccount = models.ForeignKey(ShopAccount, on_delete=models.CASCADE, null=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.PhoneNumber

    def create_sms_code(self):
        self.SMSCode = random_number(length=5)
        self.SMSCreatedTime = timezone.now()
        self.save()
        return self.SMSCode

    def check_validation_one_time_password(self):
        if (timezone.now() - self.SMSCreatedTime).seconds > OneTimePasswordValidTimeSeconds:
            return False
        return True

    def count_item_in_cart(self):
        return self.cart_set.filter(IsPaid=False).first().cartitems_set.count()

    class Meta:
        permissions = [
            ("is_shop", "is_shop, can access to shop panel to add or change product"),
        ]


def user_pre_save_received(sender, instance, *args, **kwargs):
    instance: CustomUser
    if not instance.PhoneNumber:
        instance.PhoneNumber = instance.username


pre_save.connect(user_pre_save_received, CustomUser)
