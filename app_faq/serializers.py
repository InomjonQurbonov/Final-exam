from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from app_faq.models import Faq


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'


class GetFaqSerializer(serializers.ModelSerializer):
    get_language = SerializerMethodField('get_lang')

    class Meta:
        model = Faq
        fields = ['id', 'get_language']

    def get_lang(self, obj):
        try:
            lang = self.context['request'].GET.get('lang')
            if lang == 'rus':
                question = obj.question_rus
                answer = obj.answer_rus
                return question, answer
            elif lang == 'eng':
                question = obj.question_eng
                answer = obj.answer_eng
                return question, answer
            question = obj.question_uzb
            answer = obj.answer_uzb
            return question, answer
        except:
            question = obj.question_uzb
            answer = obj.answer_uzb
            return question, answer

