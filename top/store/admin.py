from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description','price', 'is_new','is_discounted','category','brand')
    list_display_links =('name', 'ctegory', 'brand')
    search_fields = ('name', 'slug', 'description','price', 'is_new','is_discounted','category','brand')
    
class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
                           
admin.site.register(Product, SlugAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(SliderImage)
admin.site.register(Guest)
admin.site.register(CartItem)


