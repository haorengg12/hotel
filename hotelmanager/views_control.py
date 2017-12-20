from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators import csrf
import re
from hotelmanager.models import Customer
from hotelmanager.models import Bookinfo
from hotelmanager.models import Checkinfo
from hotelmanager.models import Price
import time
from django.db import connection
from django.contrib.auth.hashers import make_password, check_password


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
                pwd_s = make_password(pwd)#密码加密
                print(pwd_s)
                cus = Customer(cus_phone=phone_num, cus_password=pwd_s)
                cus.save()
                cus_id = Customer.objects.get(cus_phone=phone_num).cus_id
                request.session['cus_id'] = cus_id
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
        print(pwd_query)

    except:
        print("in login except")
        context['info'] = "帐号不存在"
        return render(request, "login.html", context)
    else:
        # print()pwd == pwd_query
        if check_password(pwd,pwd_query):#密码校验
            cus_id = Customer.objects.get(cus_phone=phone_num).cus_id
            request.session['user'] = phone_num
            request.session['cus_id'] = cus_id
            return HttpResponseRedirect("indexpage")
        else:
            print(Customer.objects.get(cus_phone=phone_num))
            context['info'] = "用户名或密码不正确"
            return render(request, "login.html", context)


def check_reserve(request):
    # 获取POST数据
    id_num = request.POST['id_num']
    book_phone = request.POST['book_phone']
    num = request.POST['num']
    price = request.POST['price']
    datein = request.POST['datein']
    dateout = request.POST['dateout']
    cus_id = request.session['cus_id']
    # --------
    context = {}
    book_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    # 将POST数据复制到context字典中，用来进行容错控制

    for k in request.POST.keys():
        context[k] = request.POST[k]
    # 将价格表放入context字典，用来进行容错控制
    price_record = Price.objects.all()
    for var in price_record:
        context[var.room_level] = var.room_price
    # -----------

    # 正则验证身份证号码和手机号码
    if not (re.match(r'^\d\d\d\d\d\d\d\d\d\d\d$', book_phone)):
        context['info'] = "请输入11位手机号码"
        print("in match statement")
        return render(request, "reserve.html", context)
    if not (re.match(r'^\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d$', id_num)):
        context['info'] = "请输入18位身份证号码"
        print("in match statement")
        return render(request, "reserve.html", context)

    # 将订单信息存入表单
    bookinfo = Bookinfo(cus_id=cus_id, book_time=book_time, book_num=num, book_idnum=id_num, book_phone=book_phone,
                        book_price=price)
    bookinfo.save()

    # 查询剩余房间
    lv = ('std_low', 'std_mid', 'std_high', 'double_low', 'double_mid', 'double_high')
    bookId = Bookinfo.objects.get(book_time=book_time).book_id
    cursor = connection.cursor()
    for i in range(6):
        sql = "SELECT room_id FROM room WHERE room_id NOT IN ( SELECT room_id FROM checkinfo WHERE  check_checkInTime <= '" + datein + "'  and check_leavetime > '" + datein + "' ) AND room_level = '" + \
              lv[i] + "'; "
        cursor.execute(sql)
        row = cursor.fetchall()
        print(row)
        temp = str(i + 1)
        r_num = int(request.POST["lv" + temp])
        print(r_num)
        # 将入住表存入数据库
        if r_num != 0:
            for j in range(r_num):  # 此处需要考虑并发控制
                check = Checkinfo(book_id=bookId, check_phone=book_phone, check_leavetime=dateout,
                                  check_checkintime=datein, check_statu='pre', room_id=row[j][0])
                check.save()

    return HttpResponseRedirect("transition")
