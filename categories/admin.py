from django.contrib import admin

from .models import Category, Expenses, Income, Subcategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'name']


@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['category', 'subcategory', 'amount', 'created_at',
                    'description']
    list_filter = ['category', 'amount']


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ['category', 'subcategory', 'amount', 'created_at',
                    'description']
    list_filter = ['category', 'amount']
