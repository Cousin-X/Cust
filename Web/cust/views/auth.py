""""中间件 阻止没有登录跳转后台"""
from django.utils.deprecation import MiddlewareMixin
class Authmiddleware(MiddlewareMixin):

    def process_requesr(self,request):

        return 