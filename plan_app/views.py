from rest_framework import generics

from .models import Plan,ClassType
from .serializers import PlanDetailSerializer,ClassTypeListSerializer

class PlanDetailView(generics.ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanDetailSerializer

    filterset_fields = ['course']

# 根据课程分类ID获取班级类型
class ClassTypeListView(generics.ListAPIView):
    queryset = ClassType.objects.all()
    serializer_class = ClassTypeListSerializer

    filterset_fields = ['course']