from django.urls import path, include
from rest_framework import routers

from app_journals.views import JournalViewSet
router = routers.DefaultRouter()
router.register('journals', JournalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]