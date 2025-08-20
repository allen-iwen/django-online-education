from django.urls import path

from . import views

urlpatterns = [
    path('user_courses_name/', views.UserCourseNameListView.as_view()),
    path('user_courses_list/', views.UserCourseListView.as_view()),
    path('user_sections_list/', views.MySectionListView.as_view()),
    path('user_add_section/', views.UserAddSectionView.as_view()),
    path('user_orders/', views.OrderListView.as_view()),
]