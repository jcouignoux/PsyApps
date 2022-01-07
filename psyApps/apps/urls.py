from django.conf import settings
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('patient', views.PatientView.as_view(), name="patient"),
    path('login', views.LoginView.as_view(), name="login"),
    path('logout', views.LogoutView.as_view(), name="logout"),
    path('api/', include(('apps.api_urls', 'api'), namespace='api')),
]
