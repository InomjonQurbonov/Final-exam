from django.shortcuts import render
from rest_framework import viewsets

from app_journals.models import Journal
from app_journals.serializers import JournalSerializer, GetJournalSerializer
from rest_framework.permissions import IsAuthenticated


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetJournalSerializer
        return JournalSerializer
