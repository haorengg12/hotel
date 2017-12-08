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

    if not (re.match(r'^\d\d\d\d\d\d\d\d\d\d\d$', phone_num)):
        context['info'] = "请输入11位手机号码"
        print("in match statement")
        return render(request, "sighup.html", context)

    if pwd == pwd_:
        if not (re.match(r'\S', pwd)):
            context['info'] = "密码中不能包括空白字符"
            return render(request, "sighup.html", context)
        elif len(pwd) < 6:
            context['info'] = "密码长度必须大于6"
            return render(request, "sighup.html", context)
        else:
            try:
                # 查看数据库中是否有该帐号
                Customer.objects.get(cus_phone=phone_num).cus_phone
            except:
                # 抛出异常，说明没有
                cus = Customer(cus_phone=phone_num, cus_password=pwd)
                cus.save()
                request.session['user'] = phone_num
                print("成功")
            else:
                # 未抛出异常，说明该帐号已存在
                context['info'] = "该帐号已存在！"
                return render(request, "sighup.html", context)

        return HttpResponseRedirect("indexpage")
    else:
        context['info'] = "密码输入不一致"
        print(pwd + "  " + pwd_)
        return render(request, "sighup.html", context)


def login_control(request):
    phone_num = request.POST['phone']
    pwd = request.POST['pwd']
    context = {}
    try:
        pwd_query = Customer.objects.get(cus_phone=phone_num).cus_password

    except:
        print("in login except")
        context['info'] = "帐号不存在"
        return render(request, "login.html", context)
    else:
        if pwd == pwd_query:
            print(pwd)
            request.session['user'] = phone_num
            return HttpResponseRedirect("indexpage")
        else:
            print(Customer.objects.get(cus_phone=phone_num))
            context['info'] = "用户名或密码不正确"
            return render(request, "login.html", context)
