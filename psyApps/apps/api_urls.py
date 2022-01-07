from django.urls import path, include
from rest_framework import routers

from apps.api_views import PatientViewset, SubjectViewset

router = routers.SimpleRouter()
router.register('patient', PatientViewset, basename='patient')
router.register('subject', SubjectViewset, basename='subject')


urlpatterns = [
    #     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls))
]
