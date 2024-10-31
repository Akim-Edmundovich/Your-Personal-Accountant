from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('api/user/', views.CustomUserListView.as_view(), name='user'),

]
