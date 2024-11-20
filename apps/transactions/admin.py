from django.contrib import admin

from .models import Category, Subcategory, Transaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['type', 'name']
    list_filter = ['type', 'name']
    prepopulated_fields = {'slug': ['name']}


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['type', 'category', 'subcategory', 'amount', 'quantity',
                    'quantity_type', 'description', 'created_at']
    list_filter = ['type', 'category', 'subcategory',
                   'amount', 'created_at']


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    prepopulated_fields = {'slug': ['name']}
