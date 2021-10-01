from .models import ProductCategory


def check_category_exist(category_name: str) -> bool:
    if ProductCategory.objects.filter(Name=category_name).exists():
        return True
    return False
