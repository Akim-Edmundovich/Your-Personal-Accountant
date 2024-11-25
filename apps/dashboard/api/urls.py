from rest_framework import routers
from django.urls import path, include

from apps.dashboard.api.views import *

urlpatterns = [
    path('transactions/', TransactionList.as_view(),
         name='api_transaction'),
    path('transactions/<int:pk>/', TransactionDetail.as_view(),
         name='api_transaction_detail'),
]
