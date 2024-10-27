from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.list_transactions, name='list_transactions'),
    path('detail-transaction/<int:pk>', views.detail_transaction,
         name='detail_transaction'),
    path('update-transaction/<int:pk>', views.update_transaction,
         name='update_transaction'),
    path('delete-transaction/<int:pk>', views.delete_transaction,
         name='delete_transaction'),

    path('filter-transactions/<str:filter_type>/', views.filter_transactions,
         name='filter_transactions'),

    path('test/', views.test, name='test'),

]
