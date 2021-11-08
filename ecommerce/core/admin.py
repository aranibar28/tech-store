from django.contrib import admin
from core.models import Product, Category, CartItem

# Register models Category.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'main_picture')

# Register models Product.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'main_picture', 'category')

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'subtotal')

# Register models.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem, CartAdmin)