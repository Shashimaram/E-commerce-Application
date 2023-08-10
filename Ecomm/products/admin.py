from django.contrib import admin
from .models import Category,Products,ProductImages, SizeVariant,ColorVariant

# Register your models here.

admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImages 
    # fk_name = "product"

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    # list_display = ['product_name', 'price']
    model = ColorVariant

@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    # list_display = ['product_name', 'price']
    model = SizeVariant

admin.site.register(Products, ProductAdmin)
admin.site.register(ProductImages)