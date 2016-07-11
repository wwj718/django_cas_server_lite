#!/usr/bin/env python
# encoding: utf-8
"""Django authentication backends.
For more information visit https://docs.djangoproject.com/en/dev/topics/auth/customizing/.
"""
#from django.conf import settings
#from django.contrib.auth.models import User, check_password
from auth_backends.models import  SeuUser
from django.contrib.auth.models import User
import hashlib
class SeuBackend(object):
    '''
    from django.contrib.auth import authenticate
    lyx = authenticate(username='lyx', password='master')
    if lyx: #验证非空，需要看下django-mama-cas中怎么做
        xxx

    dir(user) or user.[tab] 列出所有属性,要少于user wwj的属性
    user.backend #u'auth_backends.backends.SeuBackend'

    wwj = authenticate(username='wwj', password='wwj')
    #u'django.contrib.auth.backends.ModelBackend'
    '''
    def password_check(password_input,raw_password):
        """
        raw_password:是数据库里存储的
        password_input:是原始字符串
        """
        return raw_password == hashlib.md5(password_input).digest()

    def authenticate(self, username=None, password=None):
        try:
            seu_user = SeuUser.objects.get(username=username)

            #if password == 'master':
            #if password == seu_user.password:
            if  self.password_check(password,seu_user.password): # 假设数据表采用了MD5加密的密码，建议使用加盐的密码存储，md5不安全！密码可能有unicode字符问题，需要编解码
                # check password from user.password ，可以在这里是有hash算法，SeuUser表的密码可以采用任意的加密
                # 参考http://zhuoqiang.me/password-storage-and-python-example.html 用户密码的存储与 Python 示例
                # 估计采用md5 sha1 sha256之类的多，采用python直接认证就可
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    #user = User(username=username,email=username+"example.com", password='get from settings.py')
                    # 密码可以来自setting，秘钥
                    user = User(username=username, password='get from settings.py')
                    #user.set_unusable_password()
                    #user.is_staff = True
                    #user.is_superuser = True
                    user.save()
                # Authentication success by returning the user
                return user
            else:
                # Authentication fails if None is returned
                return None
        except SeuUser.DoesNotExist:
            #raise
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name, and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'sha1$4e987$afbcf42e21bd417fb71db8c66b321e9fc33051de' ,如何产生

    @property
    def user_model(self):
        return SeuUser

    def authenticate(self, username=None, password=None):
        try:
            user = self.user_model.objects.get(username=username)
            if user.check_password(password): # 取决于存储的password是什么，而修改check_password函数
                return user
        except self.user_model.DoesNotExist:
            pass
        return None




    def get_user(self, user_id):
        try:
            return self.user_model.objects.get(pk=user_id)
        except self.user_model.DoesNotExist:
            return None
    """

#############
'''
import pymysql
import pymysql.cursors
class RemoteMysqlBackend(object):
    #*  建立实验库和表，给出远程可读权限
    #*  先连接远程mysql，使用python mysql驱动:https://github.com/PyMySQL/PyMySQL
    #*  远程执行用户验证，可能有sql注入漏洞，django url机制会过滤危险查询参数？
    #*  安全的用法是用orm
    connection = pymysql.connect(host='127.0.0.1', # 测试变量放到.local.setting里
                             user='cas',
                             password='wwjcas',
                             db='cas_test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    def authenticate(self, username=None, password=None):
        # username remote_user password:remote_password
        try:
            with self.connection.cursor() as cursor: # with的话就不要关闭了吧
                # 先手动执行
                sql = "SELECT `password` FROM `users` WHERE `username`=%s AND `password`=%s"
                cursor.execute(sql, (username,password))
                result = cursor.fetchone() # 判断result决定是否登录
                #result = 1
                #self.connection.close()
                if result:
                    #self.connection.close()
                    try:
                        user = User.objects.get(username=username)
                    except User.DoesNotExist:
                        user = User(username=username, password='get from settings.py')
                        user.save()
                    return user
                return None
        #finally:
        except:
            pass

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

'''
