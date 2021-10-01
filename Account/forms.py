from django import forms
from django.core import validators


class LoginTakePhoneNumberForm(forms.Form):
    PhoneNumber = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control", "placeholder": "لطفا شماره موبایل خود را وارد کنید",
            "oninput": "phone_number_to_persian()",
        }),
        label="شماره موبایل",
        required=True,
        validators=[
            validators.RegexValidator(regex="^۰۹.........$", message="شماره موبایل معتبر نیست"),
            # validators.MinLengthValidator(limit_value=11, message=""),
            # validators.MaxLengthValidator(limit_value=11, message=""),
        ],
        error_messages={
            'required': 'شماره موبایل اجباری است',
            'max_length': 'شماره موبایل نمیتواند از 11 رقتم کمتر باشد',
            'min_length': 'شماره موبایل نمیتواند از 11 رقم بیشتر باشد'
        }
    )


class LoginTakePasswordForm(forms.Form):
    Password = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control", "placeholder": "کد پیامک شده را وارد نمیایید",
            "oninput": "password_number_to_persian()",
        }),
        label="کد پیامک شده",
        required=True,
        error_messages={
            'max_length': 'رمز نمیتواند بیشتر از 20 رقم باشد',
            'min_length': 'رمز نمیتواند کمتر از پنج رقم باشد'
        },
    )
