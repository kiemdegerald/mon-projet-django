from django.contrib import admin
from .models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'description','categorie', 'image', 'date_ajout')

admin.site.register(Product,ProductAdmin)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_ajout')
admin.site.register(Category,CategoryAdmin)
