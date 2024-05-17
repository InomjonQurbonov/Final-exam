from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from app_users.models import Profile, ContactUs

UserModel = get_user_model()


class SecondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('birth_date', 'organization', 'scientific_degree', 'another_information')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    profile = SecondSerializer(required=False)

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        user = UserModel.objects.create_user(**validated_data)
        if profile_data:
            Profile.objects.create(user=user, **profile_data)
        return user

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'profile')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'first_name', 'last_name', 'email', 'date_joined', 'last_login')
        read_only_fields = ('date_joined', 'last_login')


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ContactUsSerializer(serializers.ModelSerializer):
    admin_email = serializers.EmailField(read_only=True)
    phone = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)

    class Meta:
        model = ContactUs
        fields = "__all__"


class GetContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'first_name', 'email', 'message']
