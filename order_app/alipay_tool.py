import logging
from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.domain.AlipayTradeCreateModel import AlipayTradeCreateModel
# from alipay.aop.api.request.AlipayTradeCreateRequest import AlipayTradeCreateRequest
from alipay.aop.api.request.AlipayTradePrecreateRequest import AlipayTradePrecreateRequest
from alipay.aop.api.response.AlipayTradeCreateResponse import AlipayTradeCreateResponse

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a',)
logger = logging.getLogger('')

def get_key(path:str):
    '''
        获取秘钥
    '''
    key = None
    with open(path,'r') as f:
        key = f.read()
    return key

# 实例化客户端
alipay_client_config = AlipayClientConfig()
alipay_client_config.server_url = 'https://openapi-sandbox.dl.alipaydev.com/gateway.do'
alipay_client_config.app_id = '9021000123613559'
alipay_client_config.app_private_key = get_key('./keys/app_private_key.pem')
alipay_client_config.alipay_public_key = get_key('./keys/alipay_public_key.pem')
client = DefaultAlipayClient(alipay_client_config, logger)

def get_qr(order_id,info,money):
    # 构造请求参数对象
    model = AlipayTradeCreateModel()
    model.out_trade_no = order_id
    model.total_amount = money
    model.subject = info
    request = AlipayTradePrecreateRequest(biz_model=model)
    # 设置通知回调地址
    request.notify_url = 'http://feelinglw.natapp1.cc/api/pay_callback/'
    # 执行API调用
    response_content = False
    try:
        response_content = client.execute(request)
    except Exception as e:
        print(traceback.format_exc())
    return response_content

if __name__ == '__main__':
    # print(get_key('./keys/app_private_key.pem'))
    print(get_qr('20150320010101001','IPhone18',666))