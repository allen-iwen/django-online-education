from rest_framework import serializers

from .models import Plan,ClassType

class PlanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class ClassTypeListSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name')
    icon = serializers.CharField(source='course.icon')
    class Meta:
        model = ClassType
        fields = '__all__'