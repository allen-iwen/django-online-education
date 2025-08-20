from rest_framework import serializers

from .models import UpdateCourse

# 建立获取更新课程的列表的序列化器
class UpdateCourseListSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = UpdateCourse
        fields = ['id','name','create_time','update_type']

# 建立获取更新课程的详情的序列化器
class UpdateCourseDetailSerializer(serializers.ModelSerializer):
    # 设置获取外键的字段
    # 获取课程分类的名称
    course_name = serializers.CharField(source='course.name')
    # 获取阶段的名称
    stage_name = serializers.CharField(source='stage.name')
    # 设置时间的格式
    create_time = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = UpdateCourse
        fields = '__all__'