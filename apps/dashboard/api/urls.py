from rest_framework import routers
from django.urls import path, include

from apps.dashboard.api.views import *

router = routers.DefaultRouter()
router.register('transactions', TransactionViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)
