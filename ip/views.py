from django.views import View
from django.http import HttpResponse


class IPView(View):

    def get(self, request):
        ret2 = request.META['REMOTE_ADDR']
        ret = request.META['HTTP_X_FORWARDED_FOR']
        return HttpResponse(ret, ret2)

