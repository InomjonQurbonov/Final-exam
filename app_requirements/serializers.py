from rest_framework import serializers
from app_requirements.models import Requirements


class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = '__all__'


class GetRequirementsSerializer(serializers.ModelSerializer):
    get_all = serializers.SerializerMethodField('get_lang')

    class Meta:
        model = Requirements
        fields = ['id', 'get_all']

    def get_lang(self, obj):
        try:
            lang = self.context['request'].GET.get('lang')
            if lang == 'rus':
                req_name = obj.req_name_rus
                req_description = obj.req_description_rus
                return req_name, req_description
            elif lang == 'eng':
                req_name = obj.req_name_eng
                req_description = obj.req_description_eng
                return req_name, req_description
            req_name = obj.req_name_uzb
            req_description = obj.req_description_uzb
            return req_name, req_description
        except:
            req_name = obj.req_name_uzb
            req_description = obj.req_description_uzb
            return req_name, req_description
