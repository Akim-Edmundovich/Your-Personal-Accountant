from django import forms

from .models import Category, Subcategory, Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['category', 'subcategory', 'amount',
                  'quantity', 'quantity_type', 'description', 'created_at']



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['type', 'name']


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name']

        def __init__(self, *args, **kwargs):
            super(SubcategoryForm, self).__init__(*args, **kwargs)

            self.fields['category'].disabled = True
