from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from apps.account.api.views import UserViewSet
from yourAccountment import settings

router = SimpleRouter()

router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('account/', include('django.contrib.auth.urls')),
    path('account/', include('apps.account.urls')),
    path('transaction/', include('apps.transactions.urls')),
    path('settings/', include('apps.profile_settings.urls')),
    path('dashboard/', include('apps.dashboard.urls')),

    path('api/v1/', include('apps.transactions.api.urls', namespace='api_transactions')),

    path('social-auth/',
         include('social_django.urls', namespace='social')),
]

urlpatterns += router.urls

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']
