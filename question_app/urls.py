from django.urls import path

from . import views

urlpatterns = [
    path('user_add_question/', views.QuestionAddView.as_view()),
    path('user_add_answer/', views.AnswerAddView.as_view()),
    path('questions/', views.QuestionListView.as_view()),
    path('question/<int:pk>/', views.QuestionDetailView.as_view()),
    path('question_section/', views.QuestionSectionListView.as_view()),
]