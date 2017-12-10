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
    # siglelow = request.POST["siglelow"]
    # siglemid = request.POST["siglemid"]
    # siglehigh = request.POST["siglehigh"]
    # doublelow = request.POST["doublelow"]
    # doublemid = request.POST["doublemid"]
    # doublehigh = request.POST["doublehigh"]

    # print(datein)
    # print(dateout)
    # print(doublehigh)
    cursor = connection.cursor()
    # args = ('2017/12/11', '2017/12/12', 'std_mid')
    # result = cursor.callproc("timeselect", args)

    sql = "SELECT count(*) FROM room WHERE room_id NOT IN ( SELECT room_id FROM checkinfo WHERE ( check_checkInTime < '" + datein+"' ) OR ( check_leavetime > '" + dateout+"') ) AND room_level = 'std_mid'; "
    # sql = "select * from checkinfo where check_checkInTime = '"+'2017/12/1'+"'"
    result = cursor.execute(sql)
    row = cursor.fetchone()
    json_data['siglemid_num'] = row[0]
    sql = "SELECT count(*) FROM room WHERE room_id NOT IN ( SELECT room_id FROM checkinfo WHERE ( check_checkInTime < '" + datein + "' ) OR ( check_leavetime > '" + dateout + "') ) AND room_level = 'std_low'; "
    result = cursor.execute(sql)
    row = cursor.fetchone()
    json_data['siglelow_num'] = row[0]
    sql = "SELECT count(*) FROM room WHERE room_id NOT IN ( SELECT room_id FROM checkinfo WHERE ( check_checkInTime < '" + datein + "' ) OR ( check_leavetime > '" + dateout + "') ) AND room_level = 'std_high'; "
    result = cursor.execute(sql)
    row = cursor.fetchone()
    json_data['siglehigh_num'] = row[0]
    sql = "SELECT count(*) FROM room WHERE room_id NOT IN ( SELECT room_id FROM checkinfo WHERE ( check_checkInTime < '" + datein + "' ) OR ( check_leavetime > '" + dateout + "') ) AND room_level = 'double_low'; "
    result = cursor.execute(sql)
    row = cursor.fetchone()
    json_data['doublelow_num'] = row[0]
    sql = "SELECT count(*) FROM room WHERE room_id NOT IN ( SELECT room_id FROM checkinfo WHERE ( check_checkInTime < '" + datein + "' ) OR ( check_leavetime > '" + dateout + "') ) AND room_level = 'double_mid'; "
    result = cursor.execute(sql)
    row = cursor.fetchone()
    json_data['doublemid_num'] = row[0]
    sql = "SELECT count(*) FROM room WHERE room_id NOT IN ( SELECT room_id FROM checkinfo WHERE ( check_checkInTime < '" + datein + "' ) OR ( check_leavetime > '" + dateout + "') ) AND room_level = 'double_high'; "
    result = cursor.execute(sql)
    row = cursor.fetchone()
    json_data['doublehigh_num'] = row[0]

    cursor.execute("COMMIT")
    # print(row)
    cursor.close()

    return JsonResponse(json_data)
