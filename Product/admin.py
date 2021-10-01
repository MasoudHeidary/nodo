from django.contrib import admin

from .models import ProductCategory, Product, SubProduct


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['Name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Writer', 'Slug', 'display_category_name', 'Image', 'Active']
    list_editable = ['Active']

    @admin.display(description="product category")
    def display_category_name(self, obj: Product):
        list_of_category = list()
        for cat in obj.ToCategory.all():
            cat: ProductCategory
            list_of_category.append(cat.Name)
        return list_of_category


@admin.register(SubProduct)
class SubProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'to_product', 'to_shop', 'Price', 'Number']

    @admin.display(description="to product")
    def to_product(self, obj: SubProduct):
        return obj.ToProduct.Name

    @admin.display(description="to shop")
    def to_shop(self, obj: SubProduct):
        return obj.ToShop.Name
