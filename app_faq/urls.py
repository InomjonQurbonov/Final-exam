from django.urls import include, path
from rest_framework import routers

from app_faq.views import FaqViewSet

router = routers.DefaultRouter()

router.register('faqs', FaqViewSet)

urlpatterns = [
    path('', include(router.urls)),
]