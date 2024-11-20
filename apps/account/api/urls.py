from rest_framework import routers

from apps.account.api.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)
