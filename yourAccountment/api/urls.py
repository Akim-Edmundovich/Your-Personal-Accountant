from django.urls import path, include

urlpatterns = [
    path('v1/', include('yourAccountment.api.v1.urls')),
]