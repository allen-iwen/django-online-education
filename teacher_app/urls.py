from django.urls import path

from . import views

urlpatterns = [
    path('teachers/', views.TeacherListView.as_view()),
]