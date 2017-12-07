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
        context['info'] = "请输入11位手机号码"
        print("in match statement")
        return render(request, "sighup.html", context)

    if pwd == pwd_:
        if not(re.match(r'\S',pwd)):
            context['info'] = "密码中不能包括空白字符"
            return render(request, "sighup.html", context)
        elif len(pwd) < 6:
            context['info'] = "密码长度必须大于6"
            return render(request, "sighup.html", context)
        else:
            cus = Customer(cus_phone=phone_num, cus_password=pwd)
            cus.save()
            print("成功")
        return HttpResponseRedirect("index")
    else:
        context['info'] = "密码输入不一致"
        print(pwd + "  " + pwd_)
        return render(request, "sighup.html", context)


def login_control(request):
    phone_num = request.POST['phone']
    pwd = request.POST['pwd']
    return HttpResponseRedirect("index")
