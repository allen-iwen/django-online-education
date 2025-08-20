from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from question_app.models import Question
from question_app.serializers import QuestionAddSerializer,AnswerAddSerializer,QuestionListSerializer,QuestionDetailSerializer
from user_app.utils import verify_token
from user_app.models import User
from course_app.models import Section

class QuestionAddView(APIView):
    def post(self, request, format=None):
        # 接收参数
        serializer = QuestionAddSerializer(data=request.data)
        # 验证参数
        if serializer.is_valid():
            # 获取用户信息
            data = verify_token(request.META.get("HTTP_AUTHORIZATION"))
            user = User.objects.filter(phone=data['phone']).first()
            # 获取课程小节信息
            section = Section.objects.get(id=serializer.validated_data['section'])
            # 创建问题
            Question.objects.create(
                title= serializer.validated_data['title'],
                content= serializer.validated_data['content'],
                section= section,
                user= user
            )
            return Response({'msg':'问题创建成功','code':201})
        else:
            return Response({'msg':'问题创建失败','code':400})

class AnswerAddView(APIView):
    def post(self,request,format=None):
        # 接收参数
        serializer = AnswerAddSerializer(data=request.data)
        # 验证参数
        if serializer.is_valid():
            # 获取用户信息
            # 获取手机号
            data = verify_token(request.META.get("HTTP_AUTHORIZATION"))
            user = User.objects.filter(phone=data['phone']).first()
            # 获取课程小节信息
            section = Section.objects.get(id=serializer.validated_data['section'])
            # 获取要回答的问题
            question = Question.objects.get(id=serializer.validated_data['question'])
            # 创建回答问题
            Question.objects.create(
                content= serializer.validated_data['content'],
                section= section,
                user= user,
                answers=question
            )
            return Response({'msg':'回答问题成功','code':201})
        else:
            return Response({'msg':'回答问题失败','code':400})

# 获取问题列表
class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.filter(answers=None).all().order_by('-create_time')
    serializer_class = QuestionListSerializer

# 获取单个问题的详情
class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer

# 获取单小节下的所有问题
class QuestionSectionListView(generics.ListAPIView):
    serializer_class = QuestionDetailSerializer

    def get_queryset(self):
        # 获取小节id
        section_id = self.request.query_params.get('section')
        # 根据小节id获取问题列表
        return Question.objects.filter(section=section_id).filter(answers=None).all().order_by('-create_time')