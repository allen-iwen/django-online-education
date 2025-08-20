from rest_framework import serializers

from .models import Teacher

# 获取教师列表
class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'