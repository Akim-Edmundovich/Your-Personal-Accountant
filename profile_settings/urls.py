from django.urls import path

from . import views

urlpatterns = [
    path('', views.settings, name='settings'),

    path('categories/', views.categories_list,
         name='categories_list'),
    path('categories-by-types/<str:type_name>/', views.categories_by_type,
         name='categories_by_type'),
    path('type/<int:pk>/category-create/', views.create_category,
         name='category_create'),
    path('category/<int:pk>/', views.detail_category,
         name='category_detail'),
    path('category/<int:pk>/update/', views.update_category,
         name='category_update'),
    path('category/<int:pk>/delete/', views.delete_category,
         name='category_delete'),

    path('category/<int:pk>/subcategories/', views.subcategories_list,
         name='subcategories_list'),
    path('category/<int:pk>/subcategory-detail/', views.subcategory_detail,
         name='subcategory_detail'),
    path('category/<int:pk>/subcategory-create/', views.subcategory_create,
         name='subcategory_create'),
    path('category/<int:pk>/subcategory-update/', views.subcategory_update,
         name='subcategory_update'),
    path('category/<int:pk>/subcategory-delete/', views.subcategory_delete,
         name='subcategory_delete'),

    path('subcategory-form/', views.subcategory_form,
         name='subcategory_form'),
    path('category-form/', views.category_form,
         name='category_form'),
]
