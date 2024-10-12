from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),
    path('transaction/', include('transactions.urls')),
    path('settings/', include('profile_settings.urls')),
    path('social-auth/',
         include('social_django.urls', namespace='social')),
]
