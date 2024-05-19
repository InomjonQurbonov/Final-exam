from django.shortcuts import render
from rest_framework import viewsets

from app_faq.models import Faq
from app_faq.serializers import FaqSerializer, GetFaqSerializer
from rest_framework.permissions import IsAdminUser


class FaqViewSet(viewsets.ModelViewSet):
    queryset = Faq.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetFaqSerializer
        return FaqSerializer


