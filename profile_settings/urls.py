from django.urls import path

from . import views

app_name = 'settings'

urlpatterns = [
    path('', views.settings, name='settings_page'),

    path('list_categories/', views.list_categories,
         name='list_categories'),
    path('create_category/', views.create_category,
         name='create_category'),
    path('update_category/<str:pk>/', views.update_category,
         name='update_category'),
    path('delete_category/<str:pk>', views.delete_category,
         name='delete_category'),

    path('create_subcategory/<str:pk>/', views.create_subcategory,
         name='create_subcategory'),
    path('update_subcategory/<str:pk>/', views.update_subcategory,
         name='update_subcategory'),
    path('delete_subcategory/<str:pk>', views.delete_subcategory,
         name='delete_subcategory'),
]
