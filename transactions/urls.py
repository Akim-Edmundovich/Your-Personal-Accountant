from django.urls import path
from . import views

urlpatterns = [
    path('add-transaction/<str:transaction_type>/', views.add_transaction, name='add_transaction'),
    path('get_categories/<str:type>/', views.get_categories,
         name='get_categories'),
    path('get_subcategories/<int:category_id>/', views.get_subcategories,
         name='get_subcategories'),

]
