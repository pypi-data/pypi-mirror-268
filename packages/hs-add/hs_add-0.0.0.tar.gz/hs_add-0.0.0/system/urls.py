from django.urls import path
from system.views import TestView

urlpatterns = [
    #   test
    path('test/', TestView.as_view()),
]
