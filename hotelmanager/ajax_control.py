from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators import csrf
import re
from hotelmanager.models import Customer
from hotelmanager.models import Checkinfo
from hotelmanager.models import Bookinfo
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

def all_check(request):
	json_data = {}
	book_id = request.POST["book_id"]
	checkinfo = Checkinfo.objects.filter(book_id=book_id)
	i = 1
	for item in checkinfo:
		json={}
		json["check_id"] = item.check_id
		json["check_statu"] = item.check_statu
		json["check_time"] = item.check_checkintime
		json["leave_time"] = item.check_leavetime
		json["room_id"] = item.room_id
		json_data[i] = json
		i += 1

	# 将所定的房间个数也返回给前台页面
	json_data[0] = i-1
	return JsonResponse(json_data)


def cus_search(request):
	json_data = {}
	if request.POST["flag"]=="name":
		cus_name = request.POST["name"]
		i=1
		try:
			Cus = Customer.objects.filter(cus_name__contains=cus_name)
		except:
			json_data[0] = 0
		else:

			for item in Cus:
				json = {}
				json["id"] = item.cus_id
				json["name"]=item.cus_name
				json["phone"]=item.cus_phone
				json_data[i]=json
				i += 1
			json_data[0] = i-1
	else:
		cus_phone = request.POST["phone"]
		i = 1
		try:
			Cus = Customer.objects.filter(cus_phone__contains=cus_phone)
		except:
			json_data[0] = 0
		else:
			for item in Cus:
				json = {}
				json["id"] = item.cus_id
				json["name"] = item.cus_name
				json["phone"] = item.cus_phone
				json_data[i] = json
				i += 1
		json_data[0] = i - 1
	return JsonResponse(json_data)


def all_reserve(request):
	json_data = {}
	cus_id = request.POST["cus_id"]
	try:
		bookinfo = Bookinfo.objects.filter(cus_id=cus_id)
	except:
		json_data[0] = 0
		return JsonResponse(json_data)
	else:

		i = 1
		for item in bookinfo:
			json = {}
			json["book_id"] = item.book_id
			json["book_time"] = item.book_time
			json["book_price"] = item.book_price
			json["book_num"] = item.book_num
			json_data[i] = json
			i += 1

		# 将所定的房间个数也返回给前台页面
		json_data[0] = i - 1
		return JsonResponse(json_data)


























