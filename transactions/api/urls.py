from django.urls import path
from transactions.api.views import *

app_name = 'api'

urlpatterns = [
    path('transaction/', TransactionListView.as_view(),
         name='transaction'),
    path('category/', CategoryListView.as_view(),
         name='category'),
    path('subcategory/', SubcategoryListView.as_view(),
         name='subcategory'),

]
