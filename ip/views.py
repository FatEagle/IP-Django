from django.views import View
from django.http import HttpResponse


class IPView(View):

    def get(self, request):
        return HttpResponse('result')

