from django import forms

from .models import Transaction, Category, Subcategory


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'quantity', 'quantity_type', 'description']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']

        def __init__(self, *args, **kwargs):
            super(SubcategoryForm, self).__init__(*args, **kwargs)

            self.fields['category'].disabled = True
