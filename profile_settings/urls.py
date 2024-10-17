from django.urls import path

from . import views

app_name = 'settings'

urlpatterns = [
    path('', views.settings, name='settings_page'),
    path('categories-list/', views.categories_list,
         name='categories_list'),
    path('category-edit/<int:pk>/', views.category_edit,
         name='category_edit'),

    path('create_category/', views.create_category,
         name='create_category'),
    path('update_category/<int:pk>/', views.update_category,
         name='update_category'),
    path('delete_category/<int:pk>', views.delete_category,
         name='delete_category'),

    path('create_subcategory/<int:pk>/', views.create_subcategory,
         name='create_subcategory'),
    path('update_subcategory/<int:pk>/', views.update_subcategory,
         name='update_subcategory'),
    path('delete_subcategory/<int:pk>', views.delete_subcategory,
         name='delete_subcategory'),
]
