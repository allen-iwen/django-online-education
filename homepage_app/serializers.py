from rest_framework import serializers

from .models import RotationChart,FeatureService

# 1.创建序列化器类-轮播图
class RotationChartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RotationChart
        fields = '__all__'


class FeatureServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureService
        fields = '__all__'