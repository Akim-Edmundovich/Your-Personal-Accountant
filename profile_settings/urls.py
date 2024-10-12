from django.urls import path

from . import views

urlpatterns = [
    path('', views.settings, name='settings'),
    path('categories-by-type/', views.categories_by_type,
         name='categories_by_type'),

    path('categories/<str:type_name>/', views.categories_list,
         name='categories_list'),
    path('type/<str:type_name>/category-create/', views.category_create,
         name='category_create'),
    path('category/<int:category_pk>/', views.detail_category,
         name='category_detail'),
    path('category/<int:pk>/update/', views.update_category,
         name='category_update'),
    path('category/<int:category_pk>/delete/', views.delete_category,
         name='category_delete'),
    path('category-settings/', views.category_settings,
         name='category_settings'),

    path('category/<int:category_pk>/subcategories/', views.subcategories_list,
         name='subcategories_list'),
    path('category/<int:category_pk>/subcategory-detail/',
         views.subcategory_detail,
         name='subcategory_detail'),
    path('category/<int:category_pk>/subcategory-create/',
         views.subcategory_create,
         name='subcategory_create'),
    path('category/<int:category_pk>/subcategory-update/',
         views.subcategory_update,
         name='subcategory_update'),
    path('category/<int:category_pk>/subcategory-delete/',
         views.subcategory_delete,
         name='subcategory_delete'),

    path('subcategory-form/', views.subcategory_form,
         name='subcategory_form'),
    path('category-form/', views.category_form,
         name='category_form'),
]
