from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators import csrf
import re
from hotelmanager.models import Customer
from django.db import connection
from datetime import datetime


def search_room(request):
    json_data = {}
    datein = request.POST["datein"]
    dateout = request.POST["dateout"]
    cursor = connection.cursor()
    lv = ('std_low', 'std_mid', 'std_high', 'double_low', 'double_mid', 'double_high')
    json_index = ('siglelow_num', 'siglemid_num', 'siglehigh_num', 'doublelow_num', 'doublemid_num', 'doublehigh_num')

    for i in range(6):
        sql = "SELECT count(*) FROM room WHERE room_id NOT IN ( SELECT room_id FROM checkinfo WHERE  check_checkInTime <= '" + dateout + "'  and check_leavetime > '" + datein + "' ) AND room_level = '" + \
              lv[i] + "'; "
        result = cursor.execute(sql)
        row = cursor.fetchone()
        print(row)
        json_data[json_index[i]] = row[0]
    cursor.execute("COMMIT")
    # print(row)
    cursor.close()

    return JsonResponse(json_data)


def myinfo_update(request):
    print("in myinfo_update")
    json_data = {}
    cus_pwd = request.POST['pwd']
    cus_name = request.POST['cus_name']
    id_num = request.POST['id_num']
    print(cus_pwd)
    print(cus_name)
    print(id_num)
    if not (re.match(r'\S', cus_pwd)):
        json_data['info'] = "密码中不能包括空白字符"
        print(json_data)
        return JsonResponse(json_data)
    elif len(cus_pwd) < 6:
        json_data['info'] = "密码长度必须大于6"
        print(json_data)
        return JsonResponse(json_data)
    else:

        # 抛出异常，说明没有
        cus = Customer.objects.get(cus_id=request.session['cus_id'])
        cus.cus_password = cus_pwd
        cus.cus_name = cus_name
        cus.id_num = id_num
        cus.save()
        print("成功")
        json_data['cus_name'] = cus_name
        json_data['id_num'] = id_num
        json_data['info'] = "修改成功"
        print(json_data)
        return JsonResponse(json_data)


