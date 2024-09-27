from django import forms
from .models import Transaction
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'quantity', 'quantity_type', 'description']

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'

        # Настройка макета формы
        self.helper.layout = Layout(
            Div(
                Field('amount', css_class='form-control',
                      style='width: 100px;', placeholder='Amount'),

            ),
            Div(
                Field('quantity', css_class='form-control',
                      style='width: 100px;', placeholder='Quantity'),
                Field('quantity_type', css_class='form-control',
                      style='width: 100px;', placeholder='Quantity Type'),
                css_class='form-row'
            ),
            Div(
                Field('description', css_class='form-control',
                      style='width: 100px;', placeholder='Description'),

            ),
        )

        # Убираем метки
        for field in self.fields.values():
            field.label = ''
