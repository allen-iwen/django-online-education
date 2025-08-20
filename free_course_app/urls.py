from django.urls import path

from . import views

urlpatterns = [
    path('free_courses/', views.FreeCourseListAPIView.as_view()),
]