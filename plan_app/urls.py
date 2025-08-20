from django.urls import path

from plan_app import views

urlpatterns = [
    path('plan/',views.PlanDetailView.as_view()),
    path('class_type/',views.ClassTypeListView.as_view()),
]