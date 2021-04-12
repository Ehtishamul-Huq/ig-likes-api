from rest_framework import serializers
from userproject.models import Project, Experience, Education

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'user', 'title', 'start_date', 'end_date')

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('id', 'user', 'company_name', 'start_date', 'end_date')

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('id', 'user', 'degree', 'start_date', 'end_date')