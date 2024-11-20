from rest_framework.routers import SimpleRouter

from apps.transactions.api.views import *

router = SimpleRouter()

app_name = 'api_transactions'

router.register(r'transactions', TransactionViewSet, basename='transaction'),
router.register(r'categories', CategoryViewSet, basename='category'),
router.register(r'subcategories', SubcategoryViewSet, basename='subcategory'),

urlpatterns = router.urls
