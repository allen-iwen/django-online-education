from rest_framework import status
# from rest_framework.response import Response
from django.http import JsonResponse

from  .utils import verify_token

# 用于判断用户是否登录
class LoginRequiredMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        # 判断用户访问的接口是否是和用户相关的接口
        if request.path.startswith('/api/user'):
        # 判断是否登录, 通过true,没通过就是false
            if not verify_token(request.META.get('HTTP_AUTHORIZATION')):
                # 没用登录，或者验证失败，返回请登录响应
                # return Response({  这个不让用
                #     'code':status.HTTP_401_UNAUTHORIZED,
                #     'msg':'请登录'
                # })
                return JsonResponse(
                    {
                    'code':status.HTTP_401_UNAUTHORIZED,
                    'msg':'请登录',
                    }, 
                    json_dumps_params={'ensure_ascii':False}
                    )
        # 登录了，或者验证成功，继续执行后续的代码
        return self.get_response(request)
