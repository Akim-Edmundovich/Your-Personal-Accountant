from django.urls import path

from . import views

app_name = 'settings'

urlpatterns = [
    path('', views.settings, name='settings_page'),
    path('categories-list/', views.categories_list,
         name='categories_list'),
    path('category-edit/<int:pk>/', views.category_edit,
         name='category_edit'),

    path('subcategory-edit/<int:subcategory_pk>/<int:category_pk>/',
         views.subcategory_edit,
         name='subcategory_edit'),
    path('subcategory-delete/<int:subcategory_pk>/', views.subcategory_delete,
         name='subcategory_delete'),
]
