from django.urls import path

from . import views

urlpatterns = [
    path('update_course/', views.UpdateCourseListView.as_view()),
    path('update_course/<int:pk>/', views.UpdateCourseDetailView.as_view()),
]