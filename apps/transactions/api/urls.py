from rest_framework import routers

from apps.transactions.api.views import *

router = routers.DefaultRouter()

app_name = 'api_transactions'

# router.register('transactions', TransactionViewSet),
router.register('categories', CategoryViewSet),
router.register('subcategories', SubcategoryViewSet),

urlpatterns = []

urlpatterns.extend(router.urls)
