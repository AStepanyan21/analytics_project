from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "discounted_price",
        "rating",
        "reviews_count",
        "created_at",
    )
    list_filter = ("rating", "reviews_count")
