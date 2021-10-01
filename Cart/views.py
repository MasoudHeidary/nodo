from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.utils import timezone

from Product.models import SubProduct

from .models import Cart, CartItems, ShippingAddress
from .forms import ShippingDetailForm


@login_required(login_url="Account:LoginTakePhoneNumber")
def add_to_cart(request, sub_product_id, count):
    if count < 0:
        count = 1

    user = request.user
    cart = Cart.objects.get_or_create(ToUser=user, IsPaid=False)[0]

    sub_product = get_object_or_404(SubProduct, id=sub_product_id)

    CartItems.objects.update_or_create(ToCart=cart,
                                       ToSubProduct=sub_product,
                                       Price=sub_product.Price,
                                       Count=count)
    # return redirect('Product:ProductList')
    return redirect('Cart:Cart')


@login_required(login_url="Account:LoginTakePhoneNumber")
def cart_page(request):
    user = request.user
    cart = Cart.objects.get_or_create(ToUser=user, IsPaid=False)[0]

    shipping_address = ShippingAddress.objects.filter(ToCart=cart).first()
    shipping_detail_form = ShippingDetailForm(request.POST or None,
                                              initial=shipping_address.__dict__ if shipping_address else None)
    if shipping_detail_form.is_valid():
        data = shipping_detail_form.cleaned_data

        defaults = {
            "State": data.get('State'),
            "City": data.get('City'),
            "Address": data.get('Address'),
            "HouseNumber": data.get('HouseNumber'),
            "FloorNumber": data.get('FloorNumber'),
            "ZipCode": data.get('ZipCode'),
        }
        ShippingAddress.objects.update_or_create(
            ToCart=cart,
            defaults=defaults
        )

        return redirect("Cart:Receipt")

    context = {
        'Cart': cart,
        'Form': shipping_detail_form
    }
    return render(request, 'Cart/Cart.html', context)


@login_required(login_url="Account:LoginTakePhoneNumber")
def cart_page_increase_count(request, sub_product_id, count):
    user = request.user
    cart = Cart.objects.get_or_create(ToUser=user, IsPaid=False)[0]
    sub_product = get_object_or_404(SubProduct, id=sub_product_id)
    cart_item = get_object_or_404(CartItems, ToCart=cart, ToSubProduct=sub_product)

    cart_item.Count += 1
    cart_item.save()
    return HttpResponse()


@login_required(login_url="Account:LoginTakePhoneNumber")
def cart_page_decrease_count(request, sub_product_id, count):
    if count < 0:
        count = 1
    user = request.user
    cart = Cart.objects.get_or_create(ToUser=user, IsPaid=False)[0]
    sub_product = get_object_or_404(SubProduct, id=sub_product_id)
    cart_item = get_object_or_404(CartItems, ToCart=cart, ToSubProduct=sub_product)

    if count != 1:
        cart_item.Count -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return HttpResponse()


@login_required(login_url="Account:LoginTakePhoneNumber")
def cart_receipt_page(request):
    user = request.user
    cart = get_object_or_404(Cart, ToUser=user, IsPaid=False)

    try:
        shipping_address = cart.shippingaddress
    except:
        raise Http404()

    context = {
        "Cart": cart,
        "ShippingAddress": shipping_address
    }
    return render(request, 'Cart/CartReceipt.html', context)


@login_required(login_url="Account:LoginTakePhoneNumber")
def cart_pay(request):
    user = request.user
    cart = get_object_or_404(Cart, ToUser=user, IsPaid=False)

    cart.IsPaid = True
    cart.PaymentDate = timezone.localtime()
    cart.save()
    return redirect('Root:Home')


class OldCartListView(LoginRequiredMixin, ListView):
    login_url = "Account:LoginTakePhoneNumber"
    model = Cart
    template_name = 'Cart/OldCartList.html'

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(ToUser=user, IsPaid=True)


class OldCartDetailView(LoginRequiredMixin, DetailView):
    login_url = "Account:LoginTakePhoneNumber"
    model = Cart
    template_name = "Cart/OldCartDetail.html"

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(ToUser=user, IsPaid=True)
