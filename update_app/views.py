from rest_framework import generics

from .models import UpdateCourse
from .serializers import UpdateCourseListSerializer, UpdateCourseDetailSerializer

# 获取课程更新列表的视图
class UpdateCourseListView(generics.ListAPIView):
    queryset = UpdateCourse.objects.all().order_by('-create_time')
    serializer_class = UpdateCourseListSerializer

# 获取课程更新详情的视图
class UpdateCourseDetailView(generics.RetrieveAPIView):
    queryset = UpdateCourse.objects.all()
    serializer_class = UpdateCourseDetailSerializer