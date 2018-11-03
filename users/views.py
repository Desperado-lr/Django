from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.urls import reverse


def index(request):
    """
    index视图
    :param request:包含了请求信息的请求对象
    :return: 响应对象
    """

    return HttpResponse("hello Mac")


def say(request):
    url = reverse('users:syyy')
    print(url)
    return HttpResponse("say")


def sayhello(request):
    return HttpResponse("sayhello")
