from django.urls import path

from . import views

urlpatterns = [
    path('', views.settings, name='settings'),
]

category_url = [
    path('categories/', views.categories_list, name='categories_list'),
    path('category/create/', views.create_category, name='category_create'),
    path('category/<int:pk>/', views.detail_category, name='category_detail'),
    path('category/<int:pk>/update/', views.update_category,
         name='category_update'),
    path('category/<int:pk>/delete/', views.delete_category,
         name='category_delete'),
]

subcategory_url = [
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
]

urlpatterns.extend(category_url)
urlpatterns.extend(subcategory_url)
