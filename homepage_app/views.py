from rest_framework import generics

from .models import RotationChart,FeatureService
from .serializers import RotationChartListSerializer,FeatureServiceListSerializer

# 建立获取轮播图列表视图
class RotationChartListAPIView(generics.ListAPIView):
    queryset = RotationChart.objects.all().order_by('-id')
    serializer_class = RotationChartListSerializer

# 建立服务特色列表视图
class FeatureServiceListAPIView(generics.ListAPIView):
    queryset = FeatureService.objects.all().order_by('-id')
    serializer_class = FeatureServiceListSerializer