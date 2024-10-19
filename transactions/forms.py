from django.forms import ModelForm, Textarea

from .models import Transaction, Category, Subcategory


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['category', 'subcategory', 'amount',
                  'quantity', 'quantity_type', 'description', 'created_at']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['type', 'name']


class SubcategoryForm(ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name']


        def __init__(self, *args, **kwargs):
            super(SubcategoryForm, self).__init__(*args, **kwargs)

            self.fields['category'].disabled = True
