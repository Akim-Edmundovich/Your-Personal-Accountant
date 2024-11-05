from django.urls import path

from . import views

app_name = 'settings'

urlpatterns = [
    path('', views.settings, name='settings_page'),

    path('profile-edit-page/', views.profile_edit_page,
         name='profile_edit_page'),
    path('edit-email/', views.email_edit,
         name='email_edit'),

    path('page-categories/', views.page_categories,
         name='page_categories'),
    path('page_update_category/<int:pk>/', views.page_update_category,
         name='page_update_category'),

    path('create-category/', views.page_categories,
         name='page_categories'),
    path('update-category/<int:pk>/', views.update_category,
         name='update_category'),
    path('delete-category/<str:pk>', views.delete_category,
         name='delete_category'),

    path('create-subcategory/', views.create_subcategory,
         name='create_subcategory'),
    path('create-subcategory/', views.create_subcategory,
         name='create_subcategory'),

    path('update-subcategory/<str:pk>/', views.update_subcategory,
         name='update_subcategory'),
    path('delete-subcategory/<str:pk>', views.delete_subcategory,
         name='delete_subcategory'),
]
