from django import forms


class CartItemForm(forms.Form):
    # Count = forms.IntegerField(
    #     widget=forms.NumberInput(attrs={
    #         "class": "mtext-104 cl3 txt-center num-product"
    #     })
    # )
    pass



class ShippingDetailForm(forms.Form):
    State = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "stext-111 cl8 plh3 size-111 p-lr-15", "placeholder": "استان"
        }),
        label="استان",
        max_length=30,
        error_messages={
            'required': 'نام استان ضروری است',
            'max_length': 'نام استان نمی تواند بیشتر از ۳۰ حرف باشد'
        }
    )

    City = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "stext-111 cl8 plh3 size-111 p-lr-15", "placeholder": "شهر"
        }),
        label="شهر",
        max_length=30,
        error_messages={
            'required': 'نام شهر ضروری است',
            'max_length': 'نام شهر نمی تواند بیشتر از ۳۰ حرف باشد'
        }
    )

    Address = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "stext-111 cl8 plh3 size-111 p-lr-15", "placeholder": "آدرس پستی"
        }),
        label="آدرس پستی",
        max_length=250,
        error_messages={
            'required': 'آدرس ضروری است',
            'max_length': 'آدرس نمی تواند بیشتر از ۲۵۰ حرف باشد'
        }
    )

    HouseNumber = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "stext-111 cl8 plh3 size-111 p-lr-15", "placeholder": "پلاک"
        }),
        label="پلاک",
        max_length=5,
        error_messages={
            'required': 'پلاک ضروری است',
            'max_length': 'پلاک نمی تواند بیشتر از ۵ حرف باشد'
        }
    )

    FloorNumber = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "stext-111 cl8 plh3 size-111 p-lr-15", "placeholder": "طبقه"
        }),
        label="طبقه",
        max_length=3,
        error_messages={
            'required': 'طبقه ضروری است',
            'max_length': 'طبقه نمی تواند بیشتر از ۳ حرف باشد'
        }
    )

    ZipCode = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "stext-111 cl8 plh3 size-111 p-lr-15", "placeholder": "کد پستی"
        }),
        label="کد پستی بدون خط تیره",
        min_length=10,
        max_length=10,
        error_messages={
            'required': 'کدپستی ضروری است',
            'max_length': 'کدپستی باید ۱۰ حرف باشد',
            'min_length': 'کدپستی باید ۱۰ حرف باشد'
        }
    )
