from django.urls import path

from . import views

urlpatterns = [
    path('rotation_chart/', views.RotationChartListAPIView.as_view()),
    path('feature_service/', views.FeatureServiceListAPIView.as_view()),
]