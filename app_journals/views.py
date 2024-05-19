from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from app_journals.models import Journal
from app_journals.serializers import JournalSerializer, GetJournalSerializer
from rest_framework.permissions import IsAuthenticated
from app_journals.filters import JournalFilter


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = JournalFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetJournalSerializer
        return JournalSerializer

    def get_queryset(self):
        search_query = self.request.GET.get("search", None)
        if search_query:
            return Journal.objects.filter(
                journal_title_uz__icontains=search_query
            ) | Journal.objects.filter(
                journal_title_ru__icontains=search_query
            ) | Journal.objects.filter(
                journal_title_en__icontains=search_query
            ) | Journal.objects.filter(
                journal_description_uz__icontains=search_query
            ) | Journal.objects.filter(
                journal_description_ru__icontains=search_query
            ) | Journal.objects.filter(
                journal_description_en__icontains=search_query
            ) | Journal.objects.filter(
                journal_tegs__icontains=search_query
            )
        return Journal.objects.all()