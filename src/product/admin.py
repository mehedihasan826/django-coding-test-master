from django.contrib import admin
from .models import Product, ProductVariantPrice, Variant

admin.site.register(Product)
admin.site.register(ProductVariantPrice)
admin.site.register(Variant)

