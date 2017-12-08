from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators import csrf
import re
from hotelmanager.models import Customer


def search_room(request):
    json_data = {}
    datein = request.POST["datein"]
    dateout = request.POST["dateout"]
    siglelow = request.POST["siglelow"]
    siglemid = request.POST["siglemid"]
    siglehigh = request.POST["siglehigh"]
    doublelow = request.POST["doublelow"]
    doublemid = request.POST["doublemid"]
    doublehigh = request.POST["doublehigh"]

    print(datein)
    print(siglehigh)
    print(doublehigh)

    return JsonResponse(json_data)
