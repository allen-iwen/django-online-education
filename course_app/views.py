from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count

from .models import Course,Stage,Chapter,Section
from .serializers import CourseListSerializer,StageListSerializer,ChapterListSerializer,SectionListSerializer,StageDetailSerializer


class ResultsSetPagination(PageNumberPagination):
    '''
    自定义分页器
    '''
    page_query_param = 'page'
    page_size_query_param = 'size'
    page_size = 10

# Create your views here.
class CourseListView(generics.ListAPIView):
    # queryset = Course.objects.all()
    queryset = Course.objects.annotate(
        stage_count=Count('stages'),
        chapter_count=Count('stages__chapters'),
        section_count=Count('stages__chapters__sections')
    ).values(
        'id','name','learn_info','learn_style','learn_time','supervision','icon','brief','level',
        'stage_count','chapter_count','section_count',
    )
    serializer_class = CourseListSerializer

    # 设置分页器
    pagination_class = ResultsSetPagination

class StageListView(generics.ListAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageListSerializer

    # 设置数据过滤器
    filterset_fields = ('course',)

class ChapterListView(generics.ListAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterListSerializer

    # 设置数据过滤器
    filterset_fields = ('stage',)

class SectionListView(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionListSerializer

    # 设置数据过滤器
    filterset_fields = ('chapter',)

class StageDetailView(generics.RetrieveAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageDetailSerializer