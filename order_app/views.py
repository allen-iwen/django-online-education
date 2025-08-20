from time import time
from json import loads

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order
from .serializers import OrdersSerializers
from user_app.utils import verify_token
from user_app.models import User
from plan_app.models import ClassType
from .alipay_tool import get_qr


class OrdersView(APIView):
    def post(self,request):
        '''
            订阅课程
        '''
        # 获取用户提交的数据
        serializer = OrdersSerializers(data=request.data)
        # 校验数据
        if serializer.is_valid():
            # 提取用户信息
            data = verify_token(request.META.get('HTTP_AUTHORIZATION'))
            # 获取用户详细信息
            user = User.objects.filter(phone = data.get('phone')).first()
            # 获取订阅的课程
            ct = ClassType.objects.filter(id = serializer.validated_data.get('class_type')).first()
            # 准备订单的数据
            order_id = f'{user.id}{ct.id}{int(time())}'
            # 下订单
            Order.objects.create(
                id = order_id,
                amount = ct.price,
                user = user,
                course= ct.course,
                class_type= ct,
            )
            # 获取支付二维码
            info = f'{ct.course.name}-{ct.name}-{ct.price}'
            content = get_qr(order_id,info,float(ct.price))
            # 将content数据转换为字典
            content = loads(content)
            qr_code = content.get('qr_code')
            # 返回结果
            return Response({'msg':'订阅课程成功','code':200,'url':qr_code})
        else:
            return Response(serializer.errors)

class PayCallBack(APIView):
    def post(self,request):
        # 获取订单号
        out_trade_no = request.POST.get('out_trade_no')
        # 获取支付的时间
        gmt_payment = request.POST.get('gmt_payment')
        # 获取订单支付金额
        total_amount = request.POST.get('total_amount')
        # 获取订单信息
        order = Order.objects.get(id = out_trade_no)
        # 修改订单状态
        order.order_type = 1
        order.total_amount = total_amount
        order.gmt_payment = gmt_payment
        # 保存支付信息
        order.save()
        # 返回结果
        return Response({'msg':'支付成功','code':200})