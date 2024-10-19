from django.urls import path

from . import views

app_name = 'settings'

urlpatterns = [
    path('', views.settings, name='settings_page'),

    path('categories-page/', views.categories_page,
         name='categories_page'),

    path('update-category/<str:pk>/', views.update_category,
         name='update_category'),
    path('delete-category/<str:pk>', views.delete_category,
         name='delete_category'),

    path('create-subcategory/<str:pk>/', views.create_subcategory,
         name='create_subcategory'),
    path('update-subcategory/<str:pk>/', views.update_subcategory,
         name='update_subcategory'),
    path('delete-subcategory/<str:pk>', views.delete_subcategory,
         name='delete_subcategory'),
]
