from django.contrib import admin

from products.models import Basket, Product, ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'slug', 'description', ('price', 'quantity'), 'image', 'stripe_product_price_id', 'category')
    search_fields = ('name',)
    ordering = ('price', 'name')


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0