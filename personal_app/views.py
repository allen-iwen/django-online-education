from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserCourse,UserSection
from .serializers import UserCourseNameListSerializer,UserCourseListSerializer,MySectionListSerializer,UserSectionSerializer
from user_app.utils import verify_token
from user_app.models import User
from course_app.models import Section

class UserCourseNameListView(APIView):
    def get(self, request, format=None):
        # 根据token获取用户的唯一标识
        data = verify_token(request.META.get('HTTP_AUTHORIZATION'))
        if data:
        # 根据用户的唯一标识查询用户信息
            try:
                user = User.objects.filter(phone = data.get('phone')).first()
            except Exception as e:
                return Response({'message': '用户信息有误','code':400}, status=400)
            # 根据用户信息查询对应的课程信息
            user_course = UserCourse.objects.filter(user=user)
            # 序列化数据
            serializer = UserCourseNameListSerializer(user_course, many=True)
            # 返回数据
            return Response(serializer.data)
        else:
            return Response({'message': '请先登录','code':401}, status=401)

class UserCourseListView(APIView):
    def get(self,request,format=None):
        # 根据token获取用户的唯一标识
        data = verify_token(request.META.get('HTTP_AUTHORIZATION'))
        if data:
        # 根据用户的唯一标识查询用户信息
            try:
                user = User.objects.filter(phone = data.get('phone')).first()
                # 根据用户信息查询对应的课程信息
                user_course = UserCourse.objects.filter(user=user)
                # 序列化数据
                serializer = UserCourseListSerializer(user_course, many=True)
                return Response(serializer.data)
        # 返回数据
            except Exception as e:
                return Response({'message': '用户信息有误','code':400}, status=400)
        else:
            return Response({'message': '请先登录','code':401}, status=401)

class MySectionListView(APIView):
    def get(self,request,format=None):
        # 根据token获取用户的唯一标识
        data = verify_token(request.META.get('HTTP_AUTHORIZATION'))
        if data:
        # 根据用户的唯一标识查询用户信息
            try:
                user = User.objects.filter(phone = data.get('phone')).first()
                # 根据用户信息查询对应的收藏课程
                user_section = UserSection.objects.filter(user=user)
                # 序列化数据
                serializer = MySectionListSerializer(user_section, many=True)
                # 返回数据
                return Response(serializer.data)
            except Exception as e:
                return Response({'message': '用户信息有误','code':400}, status=400)
        # 返回数据
        else:
            return Response({'message': '请先登录','code':401}, status=401)

class UserAddSectionView(APIView):
    def post(self,request,format=None):
        # 验证secion是否传递
        serializer = UserSectionSerializer(data=request.data)
        if serializer.is_valid():

            # 根据token获取用户的唯一标识
            data = verify_token(request.META.get('HTTP_AUTHORIZATION'))
            if data:
                try:
                    user = User.objects.filter(phone = data.get('phone')).first()
                    section = Section.objects.get(pk=serializer.data.get('section'))
                    # 保存用户收藏课程
                    UserSection.objects.create(user=user,section=section)
                    return Response({'message': '收藏成功','status': 200 }, status=200)
                except Exception as e:
                    return Response({'message': '用户信息有误','code':401}, status=400)
        else:
            return Response({'message': '请传递要保存的小节ID','code':401}, status=401)


from .serializers import OrderListSerializer
from rest_framework import generics
from order_app.models import Order

class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer

    def get_queryset(self):
        # 获取的用户标识信息
        data = verify_token(self.request.META.get('HTTP_AUTHORIZATION'))
        # 获取用户信息
        user = User.objects.filter(phone=data.get('phone')).first()
        # 获取用户订单信息
        queryset = Order.objects.filter(user=user)
        # 返回结果结果集
        return queryset