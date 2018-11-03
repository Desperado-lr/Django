import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

# def weather(request, city, year):
#     print(city)
#     print(year)
#     return HttpResponse("OJBK")


# weather/beijing/2018/?a=1&b=2&a=3
def weather(request, year, city):
    # print(city)
    # print(year)
    # 查询字符串参数
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')

    print(a)
    print(b)
    print(alist)

    # 表单格式
    # c = request.POST.get('c')
    # d = request.POST.get('d')
    # clist = request.POST.get('c')
    #
    # print(c)
    # print(d)
    # print(clist)
    # print(request.body)

    # JSON
    json_bytes = request.body
    json_by = json.loads(json_bytes)
    c = json_by.get('c')
    d = json_by.get('d')
    print(c)
    print(d)

    print(request.META.get('CONTENT_TYPE'))

    return HttpResponse("OJ8K")


def demo_response(request):
    request.session['user_id'] = 100
    request.session['username'] = 'python'
    # s = '{"name":"python"}'
    #
    # response = HttpResponse(s, content_type="application/json", status=400)
    #
    # response['ManYan'] = 'name'
    #
    # return response

    return JsonResponse({'city': 'beijing', 'subject': 'python'})
