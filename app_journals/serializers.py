from rest_framework import serializers
from app_journals.models import Journal


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'


class GetJournalSerializer(serializers.ModelSerializer):
    get_all = serializers.SerializerMethodField('get_lang')

    class Meta:
        model = Journal
        fields = ['id', 'journal_title_uz', 'journal_description_uz', 'journal_tegs', 'journal_file', 'journal_image', 'get_all']

    def get_lang(self, obj):
        try:
            lang = self.context['request'].GET.get('lang')
            if lang == 'ru':
                journal_title = obj.journal_title_ru
                journal_description = obj.journal_description_ru
                return journal_title, journal_description
            elif lang == 'en':
                journal_title = obj.journal_title_en
                journal_description = obj.journal_description_en
                return journal_title, journal_description
            journal_title = obj.journal_title_uzb
            journal_description = obj.journal_description_uz
            return journal_title, journal_description
        except:
            journal_title = obj.journal_title_uz
            journal_description = obj.journal_description_uz
            return journal_title, journal_description
