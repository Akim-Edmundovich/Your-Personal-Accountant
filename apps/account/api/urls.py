from django.urls import path
from rest_framework import routers

from apps.account.api.views import *

router = routers.DefaultRouter()
# router.register('users', UserViewSet)

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

urlpatterns.extend(router.urls)
