from rest_framework import generics

from .models import FreeCourse
from .serializers import FreeCourseListSerializer

class FreeCourseListAPIView(generics.ListAPIView):
    queryset = FreeCourse.objects.all()
    serializer_class = FreeCourseListSerializer