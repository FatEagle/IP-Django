from django.views import View
from django.http import HttpResponse


class IPView(View):

    def get(self, request):
        # 反向代理IP
        ret2 = request.META['REMOTE_ADDR']
        # 真正的IP
        ret = request.META['HTTP_X_FORWARDED_FOR']
        return HttpResponse("您的IP是: {}".format(ret))

