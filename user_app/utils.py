import time

import jwt

from django.conf import settings
def generate_token(data:dict):
    # 增加要加密过期时间. 现在的时间+过期时长
    data.update({'exp':settings.JWT_EXPIRE+time.time()})
    # 通过加密算法生成token
    # token = jwt.encode(data,'123456789',algorithm='HS256')
    token = jwt.encode(data,settings.JWT_SECRET_KEY,algorithm='HS256')
    # 返回token
    return token

def verify_token(token):
    # 通过解密算法验证token
    # data = jwt.decode(token,'123456789',algorithms=['HS256'])
    try:
        data = jwt.decode(token,settings.JWT_SECRET_KEY,algorithms=['HS256'])
    except Exception as e:
        return None
    '''
    # 以下的逻辑不需要我们手动实现, jwt已经帮我们实现了
    # 获取token中的过期时间
    exp_time = data.get('exp')
    # 获取当前时间
    now = time.time()
    # 判断是否过期
    if now > exp_time:
        return None
    '''
    return data

if __name__ == '__main__':
    data = {'phone':'18600112345'}
    t = generate_token(data)
    print(f'生成token:{t}')
    d = verify_token(t) 
    
    print(f'解密token:{d}')
'''
user的唯一标识 通过 加密算法 生成 token
pip install pyjwt==2.8.0
'''