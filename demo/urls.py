"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import users.urls  # 先导入 urls模块

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 添加子路由 include意思是:包括 可以传递字符串
    url(r'^users/', include('users.urls')),
    # include也可以传递应用的urls模块 但得先导入urls模块
    # url(r'^users/', include(users.urls, namespace='users')),
    url(r'^', include('reqresp.urls')),


]
