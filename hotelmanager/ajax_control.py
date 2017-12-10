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
        sql = "SELECT count(*) FROM room WHERE room_id NOT IN ( SELECT room_id FROM checkinfo WHERE  check_checkInTime <= '" + datein + "'  and check_leavetime > '" + datein + "' ) AND room_level = '"+lv[i]+"'; "
        result = cursor.execute(sql)
        row = cursor.fetchone()
        print(row)
        json_data[json_index[i]] = row[0]
    cursor.execute("COMMIT")
    # print(row)
    cursor.close()

    return JsonResponse(json_data)
