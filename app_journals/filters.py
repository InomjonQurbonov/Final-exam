import  django_filters
from app_journals.models import Journal


class JournalFilter(django_filters.FilterSet):
    class Meta:
        model = Journal
        fields = ['journal_tegs',]
