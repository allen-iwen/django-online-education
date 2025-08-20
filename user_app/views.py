from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from user_app.models import User
from user_app.serializers import RegisterSerializer,UserDetailSerializer
from .utils import generate_token
# pip install djangorestframework==3.14.0
class LoginView(APIView):
    def post(self,request):
        '''
        登录功能
        '''
        # 1.获取参数
        phone = request.data.get('phone')
        password = request.data.get('password')
        # 2.根据参数获取数据
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            # 4.1返回消息
            return Response({'code':status.HTTP_404_NOT_FOUND,'msg':'用户不存在'})
        # 3.校验密码
        if user.check_password(password):
            # 生成token
            token = generate_token({'phone':phone})
            return Response({
                'code':status.HTTP_200_OK,
                'msg':'登录成功',
                'token':token
                })
        else:
            return Response({'code':status.HTTP_400_BAD_REQUEST,'msg':'密码错误'})

class RegisterView(APIView):
    def post(self,request):
        # 1. 创建序列化器
        serializer = RegisterSerializer(data=request.data)
        # 2. 校验参数
        if serializer.is_valid():
        # 成功
        # 2.1 保存数据
            user = serializer.save()
        # 2.2 返回响应
            return Response({
                'code':status.HTTP_201_CREATED,
                'msg':'注册成功'
                })
        # 失败
        else: 
        # 2.3 返回响应
            return Response({
                'code':status.HTTP_400_BAD_REQUEST,
                'msg':f'注册失败:{serializer.errors}'
            })
            
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer