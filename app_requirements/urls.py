from django.urls import path, include
from rest_framework import routers

from app_requirements.views import RequirementsViewSet


router = routers.DefaultRouter()
router.register('requirements', RequirementsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]