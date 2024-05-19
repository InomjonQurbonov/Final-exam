from rest_framework import serializers
from app_papers.models import Papers, References, Reviews


class PapersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Papers
        fields = '__all__'


class GetPapersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Papers
        fields = '__all__'
        extra_kwargs = {
            'author': {'read_only': True},
            'paper_date': {'read_only': True},
            'paper_views': {'read_only': True},
        }

    def get_lang(self, obj):
        try:
            lang = self.context['request'].GET.get('lang')
            if lang == 'ru':
                paper_title = obj.paper_title_ru
                paper_description = obj.paper_description_ru
                paper_content = obj.paper_content_ru
                return paper_title, paper_description, paper_content
            elif lang == 'en':
                paper_title = obj.paper_title_en
                paper_description = obj.paper_description_en
                paper_content = obj.paper_content_en
                return paper_title, paper_description, paper_content
            paper_title = obj.paper_title_uzb
            paper_description = obj.paper_description_uz
            paper_content = obj.paper_content_uz
            return paper_title, paper_description, paper_content
        except:
            paper_title = obj.paper_title_uz
            paper_description = obj.paper_description_uz
            paper_content = obj.paper_content_uz
            return paper_title, paper_description, paper_content


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = References
        fields = '__all__'


class GetReferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = References
        fields = ['id', 'url', 'description']


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
        extra_kwargs = {
            'review_date': {'read_only': True},
            'review_file': {'read_only': True},
        }


class GetReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'review_text', 'review_file']
