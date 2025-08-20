import hashlib

from django.db import models

# Create your models here.
class User(models.Model):
    GENDER_CHOICES = (
        (0,'女'),
        (1,'男'),
    )

    phone = models.CharField(null=True,blank=True,max_length=11,unique=True,verbose_name='手机号')
    password = models.CharField(null=True,blank=True,max_length=32,verbose_name='密码')
    _password = models.CharField(null=True,blank=True,max_length=32,verbose_name='密码2')
    nickname = models.CharField(null=True,blank=True,max_length=32,verbose_name='昵称')
    gender = models.IntegerField(null=True,blank=True,choices=GENDER_CHOICES,verbose_name='性别')
    job_title = models.CharField(null=True,blank=True,max_length=32,verbose_name='职位')
    introduction = models.CharField(null=True,blank=True,max_length=256,verbose_name='简介')
    avatar = models.CharField(null=True,blank=True,max_length=256,verbose_name='头像')

    create_at = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True,verbose_name='更新时间')

    class Meta:
        db_table ='t_user'

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,pwd):
        # 数据加密
        self._password = hashlib.md5(pwd.encode('utf-8')).hexdigest()

    def check_password(self,raw_pwd):
        pwd = hashlib.md5(raw_pwd.encode('utf-8')).hexdigest()
        return pwd == self._password