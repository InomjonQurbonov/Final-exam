from django.urls import path, include
from rest_framework import routers

from app_papers.views import PapersViewSet, ReferenceViewSet, ReviewsViewSet

router = routers.DefaultRouter()
router.register(r'papers', PapersViewSet)
router.register(r'references', ReferenceViewSet)
router.register(r'reviews', ReviewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]