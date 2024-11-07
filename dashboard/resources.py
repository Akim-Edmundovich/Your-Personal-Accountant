from import_export import resources
from import_export.fields import Field
from import_export.widgets import DateWidget, ForeignKeyWidget

from transactions.models import Transaction, Category, Subcategory


class TransactionResource(resources.ModelResource):
    category_field = Field(attribute='category',
                           column_name='Category', )
    subcategory_field = Field(attribute='subcategory',
                              column_name='Subcategory', )
    amount_field = Field(attribute='amount',
                         column_name='Amount')
    quantity_field = Field(attribute='quantity',
                           column_name='Quantity')
    quantity_type_field = Field(attribute='quantity_type',
                                column_name='Quantity type')
    description_field = Field(attribute='description',
                              column_name='Comment')
    created_at_field = Field(attribute='created_at',
                             column_name='Date',
                             widget=DateWidget(format='%d.%m.%y'))

    class Meta:
        model = Transaction
        fields = ('category_field', 'subcategory_field',
                  'amount_field', 'quantity_field',
                  'quantity_type_field', 'description_field',
                  'created_at_field')



