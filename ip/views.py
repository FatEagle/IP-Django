import ssl
import json
# 防止冲突
from urllib import request as urllib_request

from django.views import View
from django.http import HttpResponse
from django.conf import settings


class IPView(View):

    def get(self, request):
        ip = self.__get_user_ip(request)
        address = self.__get_address_by_baidu_api(ip)

        return HttpResponse(
            "<p>您的IP是(Your IP is): {}</p><p>地理位置是: 省:{}, 市:{}</p>".format(
                ip,
                address['content']['address_detail']['province'],
                address['content']['address_detail']['city'])
        )

    @staticmethod
    def __get_user_ip(request):
        try:
            request_ip = request.META['REMOTE_ADDR']
        except KeyError:
            pass

        try:
            # 反向代理后存储的IP
            user_ip = request.META['HTTP_X_FORWARDED_FOR']
        except KeyError:
            # 局域网请求
            user_ip = None

        return user_ip or request_ip

    @staticmethod
    def __get_address_by_baidu_api(ip):
        context = ssl._create_unverified_context()
        baidu_api = 'https://api.map.baidu.com/location/ip?ip={ip}&ak={ak}&coor=bd09ll'.format(
            ip=ip,
            ak=settings.AK
        )

        address = urllib_request.urlopen(baidu_api, context=context)
        return json.load(address)

