import ssl
import json
from urllib import request as urllib_request
from urllib import parse

from django.views import View
from django.http import HttpResponse
from django.conf import settings


class IPView(View):

    def get(self, request):
        # 反向代理IP
        try:
            ret2 = request.META['REMOTE_ADDR']
        except KeyError:
            pass

        try:
            # 真正的IP
            ret = request.META['HTTP_X_FORWARDED_FOR']
        except KeyError:
            print('local')
            ret = ret2

        context = ssl._create_unverified_context()
        baidu_api = 'https://api.map.baidu.com/location/ip?ip={ip}&ak={ak}&coor=bd09ll'.format(
            ip=ret,
            ak=settings.AK
        )

        address = urllib_request.urlopen(baidu_api, context=context)
        address = json.load(address)

        return HttpResponse(
            "您的IP是(Your IP is): {}\n地理位置是: 省:{}, 市:{} ".format(
                ret,
                address['content']['address_detail']['province'],
                address['content']['address_detail']['city'])
        )

