from rest_framework import routers

from apps.dashboard.api.views import TransactionViewSet

router = routers.DefaultRouter()
router.register('transactions', TransactionViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)
