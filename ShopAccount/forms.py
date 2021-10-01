from django import forms


class AddProductForm(forms.Form):
    Publisher = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control", "placeholder": "ناشر"
        }),
        max_length=150,
        label="ناشر"
    )

    Name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control", "placeholder": "نام کالا"
        }),
        max_length=250,
        label="نام کالا",
    )

    Writer = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control", "placeholder": "نویسنده"
        }),
        max_length=150,
        label="نویسنده"
    )

    Translator = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control", "placeholder": "مترجم"
        }),
        required=False,
        max_length=150,
        label="مترجم"
    )

    Description = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control", "placeholder": "توضیحات"
        }),
        label="توضیحات"
    )

    Barcode = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control", "placeholder": "بارکد"
        }),
        max_length=100,
        label="بارکد"
    )


class AddSubProductForm(forms.Form):
    IsSecondHand = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input"
        }),
        label="دست دوم؟",
        required=False
    )

    SecondHandRate = forms.ChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control", "placeholder": "درجه کیفی محصول دسته دوم"
        }),
        choices=(
            ("N", "نو"),
            ("A+", "(A+) دست دو استفاده نشده"),
            ("A", "(A) استفاده شده بدون نوشتگی و در حد نو"),
            ("B", "(B) استفاده شده همراه نوشتگی کم با مداد"),
            ("C", "(C) استفاده شده همراه با خط خوردگی"),
        ),
        label="درجه کیفی محصول دسته دوم",
        required=False
    )

    BriefDescription = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control", "placeholder": "توضیحات کوتاه محصول"
        }),
        label="توضیحات کوتاه محصول",
        max_length=50,
        required=True
    )

    Price = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control", "placeholder": "قیمت محصول"
        }),
        label="قیمت"
    )

    Number = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "form-control", "placeholder": "تعداد موجودی"
        }),
        label="تعداد موجودی"
    )

    SellOnline = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input", "value": "1"
        }),
        label="فروش آنلاین",
        required=False
    )
