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
from hotelmanager.models import Room
from django.contrib.auth.hashers import make_password, check_password

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
		cus = Customer.objects.get(cus_id=request.session['cus_id'])
		pwd = make_password(cus_pwd)#密码加密
		cus.cus_password = pwd
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


def res_reserve(request):
	json_data = {}
	book_phone = request.POST["phone"]
	try:
		bookinfo = Bookinfo.objects.filter(book_phone__contains=book_phone)
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


def insert_check(request):
	info={}
	check_id = request.POST["check_id"]
	name = request.POST["name"]
	phone = request.POST["phone"]
	idnum = request.POST["idnum"]
	ctime = request.POST["ctime"]
	ltime = request.POST["ltime"]
	room_id = request.POST["room_id"]
	statu = request.POST["statu"]

	if name=="" or phone=="" or idnum=="" or ctime=="" or ltime=="" or room_id=="":
		info["info"] = "0"
	elif not (re.match(r'^\d\d\d\d\d\d\d\d\d\d\d$', phone)):
		info["info"] = "0"
	elif not (re.match(r'^\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d$', idnum)):
		info["info"] = "0"
	else:
		checkinfo = Checkinfo.objects.filter(check_id=check_id).update(check_name=name,check_phone=phone,check_idnum=idnum,check_leavetime=ltime,check_checkintime=ctime,check_statu=statu,room_id = room_id)
		info["info"]="1"
	return JsonResponse(info)


def get_room_by_id(request):
	json_data = {}
	room_id = request.POST["room_id"]
	if room_id == "":
		json_data[0] = 0
	else:
		cursor = connection.cursor()
		sql = "select * from room_info WHERE room_id = '"+room_id+"';"
		result = cursor.execute(sql)
		row = cursor.fetchall()
		print(row)
		index = ["room_id","name","phone","ctime","ltime","check_id","book_id","statu","level","price"]
		j=2
		for item in row:
			json = {}
			for i in range(0,10):
				json[index[i]] = item[i]
			json_data[j] = json
			j+=1
		cursor.execute("COMMIT")
		# print(row)
		cursor.close()

		json_data[0]=1
		json_data[1]=j
	return JsonResponse(json_data)

def get_room_by_date(request):
	json_data = {}
	datein = request.POST["datein"]
	dateout = request.POST["dateout"]
	if datein=="" or dateout=="":
		json_data[0] = 0
	else:
		cursor = connection.cursor()
		sql = "SELECT * FROM room_info WHERE  check_checkInTime <= '" + dateout + "'  and check_leavetime > '" + datein + "';"
		result = cursor.execute(sql)
		row = cursor.fetchall()
		index = ["room_id", "name", "phone", "ctime", "ltime", "check_id", "book_id", "statu", "level", "price"]
		j = 2
		for item in row:
			# print(item)
			json = {}
			for i in range(0, 10):
				json[index[i]] = item[i]
			json_data[j] = json
			j += 1

		cursor.execute("COMMIT")
		# print(row)
		cursor.close()

		json_data[0] = 1
		json_data[1] = j
	return JsonResponse(json_data)


def add_room(request):
	json_data={}

	room_id = request.POST['room_id']
	room_level = request.POST['room_level']

	if room_id=="" or room_level=="" or len(room_id)!=3:
		json_data["info"] = 0
	else:
		try:
			room = Room.objects.get(room_id=room_id)
		except:
			#查询失败，数据库中不存在该房间号
			add = Room(room_id=room_id,room_level=room_level)
			add.save()
			json_data["info"]=1
		else:
			room.room_id=room_id
			room.room_level=room_level
			room.save();
			json_data["info"] = 1
	return JsonResponse(json_data)


def delete_room(request):
	json_data={}

	room_id = request.POST['room_id']

	if room_id=="" or len(room_id)!=3:
		json_data["info"] = 0
	else:
		try:
			room = Room.objects.get(room_id=room_id)
		except:
			#查询失败，数据库中不存在该房间号
			json_data["info"] = 0
		else:
			room.delete()
			json_data["info"] = 1
	return JsonResponse(json_data)

def delete_check(request):
	json_data={}

	check_id = request.POST['check_id']
	try:
		check = Checkinfo.objects.get(check_id=check_id)
	except:
		#查询失败，数据库中不存在该房间号
		json_data["info"] = 0
	else:
		check.delete()
		json_data["info"] = 1
	return JsonResponse(json_data)





