from django.urls import path
from . import views

urlpatterns = [
    path('', views.settings, name='settings'),
    path('category/mine/',
         views.ManageCategoryList.as_view(),
         name='manage_category_list'),
    path('category/create/',
         views.CategoryCreateView.as_view(),
         name='category_create'),
    path('category/<int:pk>/edit/',
         views.CategoryUpdateView.as_view(),
         name='category_update'),
    path('category/<int:pk>/delete/',
         views.CategoryDeleteView.as_view(),
         name='category_delete'),

    path('category/<int:pk>/subcategory/create/',
         views.SubcategoryCreateView.as_view(),
         name='subcategory_create'),
    path('subcategory/<int:pk>/edit/',
         views.SubcategoryUpdateView.as_view(),
         name='subcategory_edit'),
    path('subcategory/<int:pk>/delete/',
         views.SubcategoryDeleteView.as_view(),
         name='subcategory_delete'),

]
