from django.shortcuts import render
from rest_framework import viewsets

from app_requirements.models import Requirements
from app_requirements.serializers import RequirementsSerializer, GetRequirementsSerializer
from rest_framework.permissions import IsAdminUser


class RequirementsViewSet(viewsets.ModelViewSet):
    queryset = Requirements.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetRequirementsSerializer
        return RequirementsSerializer
