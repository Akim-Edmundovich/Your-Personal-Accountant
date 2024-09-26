from django.urls import path
from . import views

urlpatterns = [
    path('', views.settings, name='settings'),
    path('mine/',
         views.ManageCategoryList.as_view(),
         name='manage_category_list'),
    path('create/',
         views.CategoryCreateView.as_view(),
         name='category_create'),
    path('<pk>/edit/',
         views.CategoryUpdateView.as_view(),
         name='category_update'),
    path('<pk>/delete/',
         views.CategoryDeleteView.as_view(),
         name='category_delete'),

]

