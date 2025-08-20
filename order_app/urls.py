from django.urls import path

from . import views

urlpatterns = [
    path('user_pay_couser/',views.OrdersView.as_view()),
    path('pay_callback/',views.PayCallBack.as_view()),
]