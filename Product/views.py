from django.shortcuts import render, get_object_or_404, Http404
# from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q
from urllib.parse import unquote
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product
from .util import check_category_exist


class ProductListView(ListView):
    model = Product
    template_name = 'Product/ProductListView.html'
    paginate_by = 16

    def get_queryset(self):
        query = Q(Active=True)

        category = self.kwargs.get('category')
        if category:
            query &= Q(ToCategory__Name=category)

        search = self.request.GET.get('search')
        if search:
            for i in search.split(' '):
                query &= (Q(Name__contains=i) | Q(Publisher__contains=i) |
                          Q(Writer__contains=i) | Q(Translator__contains=i))

        return Product.objects.filter(query)
        # if category:
        #     if not check_category_exist(category):
        #         raise Http404()
        #     return Product.objects.filter(ToCategory__Name=category)
        # return Product.objects.filter(Active=True)

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(ProductListView, self).get_context_data(**kwargs)
    #     return context


class ProductDetailView(DetailView):
    model = Product
    slug_field = "Slug"
    template_name = 'Product/ProductDetailView.html'

    def get_queryset(self):
        # book = Product.objects.get(id=11)
        # print(book.subproduct_set.all())

        slug = self.kwargs.get('slug')
        self.kwargs.update({"slug": unquote(slug)})

        return Product.objects.all()

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data(**kwargs)
    #     return context
