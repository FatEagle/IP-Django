from django.views import View
from django.http import HttpResponse


class IPView(View):

    def get(self, request):
        ret = request.META['HTTP_X_FORWARDED_FOR']
        return HttpResponse(ret)

