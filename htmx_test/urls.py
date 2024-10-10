from django.urls import path
from . import views

urlpatterns = [
    path('', views.opera_list, name='operas'),
    path('operas/', views.opera_clean_list, name='list_operas'),
    path('opera/<int:pk>/update/', views.update_opera, name='update_opera'),
    path('opera/<int:pk>/detail/', views.detail_opera, name='detail_opera'),
    path('opera/<int:pk>/delete/', views.delete_opera, name='delete_opera'),
    path('opera/<int:pk>/singers/', views.opera_singer_list,
         name='opera_singer_list'),

    path('opera/singers/<int:pk>/', views.opera_singer_detail,
         name='opera_singer_detail'),
    path('opera/singer/<int:pk>/update/', views.opera_singer_update,
         name='opera_singer_update'),
    path('opera/singer/<int:pk>/delete', views.singer_delete,
         name='singer_delete'),
    path('opera/create/', views.create_opera, name='create_opera'),
    path('opera/<int:pk>/singer-create/', views.opera_singer_create,
         name='opera_singer_create'),


    path('create-singer-form/', views.create_singer_form,
         name='create_singer_form'),
    path('create-opera-form/', views.create_opera_form,
         name='create_opera_form'),

]
