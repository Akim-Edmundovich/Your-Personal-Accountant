from django.contrib import admin

from .models import Category, Subcategory, Transaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['category', 'subcategory', 'amount', 'quantity',
                    'quantity_type', 'description', 'created_at']
    list_filter = ['category', 'subcategory',
                   'amount', 'created_at']


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
