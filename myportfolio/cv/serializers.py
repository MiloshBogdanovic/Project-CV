from rest_framework import serializers
from .models import UserCV, WorkHistory, Education
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')



class WorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHistory
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class UserCVSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    work_histories = WorkHistorySerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)

    class Meta:
        model = UserCV
        fields = ('id', 'user', 'bio', 'skills', 'work_histories', 'educations')        