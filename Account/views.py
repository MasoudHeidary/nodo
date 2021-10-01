from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from persiantools import digits
from utils.SMS import sms_one_time_password

from .forms import LoginTakePhoneNumberForm, LoginTakePasswordForm
from .models import CustomUser


def logout_page(request):
    if not request.user.is_authenticated:
        return redirect('Root:Home')

    logout(request)
    return redirect('Root:Home')
    # return HttpResponse("logout done")


def login_take_phone_number(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")

    take_phone_number_form = LoginTakePhoneNumberForm(request.POST or None)
    if take_phone_number_form.is_valid():
        phone_number = digits.fa_to_en(take_phone_number_form.cleaned_data.get('PhoneNumber'))
        user = CustomUser.objects.filter(username=phone_number).first()
        if not user:
            user = CustomUser.objects.create_user(username=phone_number)

        sms_code = user.create_sms_code()
        print(sms_code)
        # sms_one_time_password(phone_number, sms_code)

        return HttpResponseRedirect(reverse("Account:LoginTakePassword") + f"?phone-number={phone_number}")

    context = {
        "Form": take_phone_number_form,
    }

    return render(request, 'Account/LoginTakePhoneNumber.html', context)


def login_take_password(request):
    if request.user.is_authenticated:
        return redirect('Root:Home')

    phone_number = request.GET.get('phone-number')
    if not phone_number:
        return redirect("Account:LoginTakePhoneNumber")

    take_password_form = LoginTakePasswordForm(request.POST or None)
    if take_password_form.is_valid():
        password = digits.fa_to_en(take_password_form.cleaned_data.get('Password'))
        user = CustomUser.objects.get_user_with_one_time_password(phone_number, password)

        if user:
            login(request, user)
            return redirect('Root:Home')
        else:
            take_password_form.add_error('Password', 'رمز وارد شده صحیح نمی باشد')

    context = {
        'Form': take_password_form,
    }

    return render(request, 'Account/LoginTakePassword.html', context)
