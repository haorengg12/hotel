from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators import csrf
import re
from hotelmanager.models import Customer
# Create your views here.


def sighup_control(request):
    print("views_control:   sighup")
    phone_num = request.POST['phone']
    pwd = request.POST['pwd']
    pwd_ = request.POST['pwd_']
    context = {}

    if not(re.match(r'^\d\d\d\d\d\d\d\d\d\d\d$', phone_num)):
        info = "请输入11位手机号码"
        print("in match statement")
        return HttpResponseRedirect("sighup?info="+info)

    if pwd == pwd_:
        print(pwd+"  "+pwd_)
        cus = Customer(cus_phone=phone_num, cus_password=pwd)
        cus.save()
        success = "alert('注册成功')"
        return HttpResponseRedirect("indexpage?success="+success)

    else:
        info = "密码输入不一致"
        print(pwd + "  " + pwd_)
        return HttpResponseRedirect("indexpage?info=" + info)
