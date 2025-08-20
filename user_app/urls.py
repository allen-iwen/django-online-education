from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
]

# postman 3方工具
# vscode插件：REST Client

'''
1. AssertionError: Expected view UserDetail to be called with a URL keyword argument named "pk". Fix your URL conf, or set the `.lookup_field` attribute on the view correctly.
url地址上的参数没有定义成PK

2. AssertionError: The field 'password' was included on serializer UserDetailSerializer in the 'exclude' option, but does not match any model field.
序列化器中的字段没有在模型中定义
'''