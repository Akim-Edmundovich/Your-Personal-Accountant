from django.contrib import admin
from django.urls import path, include

from yourAccountment import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('account/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),
    path('transaction/', include('transactions.urls')),
    path('settings/', include('profile_settings.urls')),
    path('dashboard/', include('dashboard.urls')),

    path('api/', include('transactions.api.urls', namespace='api')),

    path('social-auth/',
         include('social_django.urls', namespace='social')),
]

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
