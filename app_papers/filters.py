import django_filters
from app_papers.models import Papers, References


class PapersFilter(django_filters.FilterSet):
    class Meta:
        model = Papers
        fields = ['paper_title_uz', 'paper_title_ru', 'paper_title_en', 'author', 'paper_tegs']


class ReferencesFilter(django_filters.FilterSet):
    class Meta:
        model = References
        fields = ['url', ]
