from django.urls import path
from .views import IPView

urlpatterns = [
    path('', IPView.as_view()),
]
