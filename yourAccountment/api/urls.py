from django.urls import include, path

urlpatterns = [
    path('', include('apps.transactions.api.urls')),
    path('', include('apps.dashboard.api.urls')),
    path('', include('apps.account.api.urls')),

]