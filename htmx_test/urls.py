from django.urls import path
from . import views

urlpatterns = [
    path('', views.opera_list, name='opera_list'),

    path('opera/<int:pk>/update/', views.update_opera, name='update_opera'),
    path('opera/<int:pk>/detail/', views.detail_opera, name='detail_opera'),
    path('opera/<int:pk>/delete/', views.delete_opera, name='delete_opera'),
    path('opera/create/', views.create_opera, name='create_opera'),
    path('create-opera-form/', views.create_opera_form, name='create_opera_form'),
]
