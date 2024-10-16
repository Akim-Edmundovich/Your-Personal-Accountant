from django.urls import include, path

from . import views

app_name = 'transaction'

urlpatterns = [
    path('add-transaction/', views.add_transaction,
         name='add-transaction'),

    path('get_categories/<str:type_name>/', views.get_categories,
         name='get_categories'),
    path('get_subcategories/<int:category_id>/', views.get_subcategories,
         name='get_subcategories'),

]
