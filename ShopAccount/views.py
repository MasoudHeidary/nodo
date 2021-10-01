from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views.generic.list import ListView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from Product.models import Product, SubProduct

from .forms import AddProductForm, AddSubProductForm


@permission_required('Account.is_shop', login_url="Account:LoginTakePhoneNumber")
def admin_dashboard(request):
    # shop = request.user.ToShopAccount
    # if not shop:
    #     return HttpResponse("اکانت فروشگاهی شما متصل نشده است")
    context = {

    }
    return render(request, "ShopAccount/AdminDashboard.html", context)


class AdminProductListView(PermissionRequiredMixin, ListView):
    permission_required = "Account.is_shop"
    login_url = "Account:LoginTakePhoneNumber"
    model = Product
    template_name = "ShopAccount/AdminProduct.html"
    paginate_by = 20

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            query = Q()
            for i in search.split(' '):
                query &= (Q(Name__contains=i) | Q(Publisher__contains=i) |
                          Q(Writer__contains=i) | Q(Translator__contains=i))

            return Product.objects.filter(query).distinct()
        return Product.objects.all()

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(AdminProductListView, self).get_context_data(**kwargs)
    #     return context


@permission_required('Account.is_shop', login_url="Account:LoginTakePhoneNumber")
def admin_add_product(request):
    product_form = AddProductForm(request.POST or None)

    if product_form.is_valid():
        if not request.user.ToShopAccount:
            return HttpResponse("اکانت فروشگاهی شما متصل نیست")
        data = product_form.cleaned_data

        Product.objects.create(
            Name=data.get('Name'),
            Writer=data.get('Writer'),
            Translator=data.get('Translator'),
            Publisher=data.get('Publisher'),
            Description=data.get('Description'),
            Barcode=data.get('Barcode'),
            Active=False,
        )

        return redirect("ShopAdmin:Dashboard")

    context = {
        "Form": product_form
    }
    return render(request, "ShopAccount/AdminAddProduct.html", context)


@permission_required('Account.is_shop', login_url="Account:LoginTakePhoneNumber")
def admin_add_sub_product(request, id):
    sub_product_form = AddSubProductForm(request.POST or None)

    if sub_product_form.is_valid():
        data = sub_product_form.cleaned_data
        shop = request.user.ToShopAccount
        if not shop:
            return HttpResponse("اکانت فروشگاهی شما متصل نیست")

        product = Product.objects.filter(id=id)
        if not product.exists():
            return redirect("ShopAdmin:Product")
        product = product.first()

        SubProduct.objects.create(
            IsSecondHand=data.get('IsSecondHand'),
            SecondHandRate=data.get('SecondHandRate'),
            BriefDescription=data.get("BriefDescription"),
            Price=data.get('Price'),
            Number=data.get('Number'),
            ToShop=shop,
            ToProduct=product,
            SellOnline=data.get('SellOnline')
        )

        return redirect("ShopAdmin:Product")

    context = {
        "Form": sub_product_form
    }
    return render(request, 'ShopAccount/AdminAddSubProduct.html', context)