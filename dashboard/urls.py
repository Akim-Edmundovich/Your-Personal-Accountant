from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('detail-transaction/<int:pk>', views.detail_transaction,
         name='detail_transaction'),
    path('update-transaction/<int:pk>', views.update_transaction,
         name='update_transaction'),
    path('delete-transaction/<int:pk>', views.delete_transaction,
         name='delete_transaction'),

    path('to_html_format_expenses_filter/<str:filter_type>/',
         views.to_html_format_expenses_filter,
         name='to_html_format_expenses_filter'),
    path('to_html_format_incomes_filter/<str:filter_type>/',
         views.to_html_format_incomes_filter,
         name='to_html_format_incomes_filter'),

    path('list-transactions/<str:category>/',
         views.list_transactions,
         name='list_transactions'),

    path('export-by-category/<file_format>/', views.export_order_by_category,
         name='export_order_by_category'),
    path('xlsx-formatter/<filter_type>/',
         views.to_xlsx_formatter,
         name='to_xlsx_formatter'),


]
