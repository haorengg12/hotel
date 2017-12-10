from django.shortcuts import render
from django.http import HttpResponseRedirect
from hotelmanager.models import Price

# Create your views here.


def index(request):
    context = {}
    context['img1'] = 'img/room/1.jpg'
    context['img2'] = 'img/room/2.jpg'
    context['img3'] = 'img/room/3.jpg'
    context['img4'] = 'img/room/4.jpg'
    context['img5'] = 'img/room/5.jpg'
    context['img6'] = 'img/room/6.jpg'
    user = request.session.get('user', None)
    if user is None:
        context['login'] = '登录'
        context['login_URL'] = 'login'
        return render(request, 'index.html', context)
    else:
        context['login'] = '注销'
        context['login_URL'] = 'logout'
        return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')


def loginout(request):
    del request.session['user']
    return HttpResponseRedirect("indexpage")


def sighup(request):
    return render(request, 'sighup.html')


def book(request):
    context = {}
    user = request.session.get('user', None)
    if user is None:
        context['login'] = '登录'
        context['login_URL'] = 'login'
        return HttpResponseRedirect("transition")
    else:
        context['login'] = '注销'
        context['login_URL'] = 'logout'
        return render(request, 'bookpage.html', context)


def reserve(request):
    context = {}
    user = request.session.get('user', None)
    if user is None:
        context['login'] = '登录'
        context['login_URL'] = 'login'
        return HttpResponseRedirect("transition")
    else:
        context['login'] = '注销'
        context['login_URL'] = 'logout'
        context['sl'] = request.POST["sl"]
        context['sm'] = request.POST["sm"]
        context['sh'] = request.POST["sh"]
        context['dl'] = request.POST["dl"]
        context['dm'] = request.POST["dm"]
        context['dh'] = request.POST["dh"]

        price = Price.objects.all()
        print(price)

        return render(request, 'reserve.html', context)


def myreserve(request):
    context = {}
    user = request.session.get('user', None)
    if user is None:
        context['login'] = '登录'
        context['login_URL'] = 'login'
        return HttpResponseRedirect("transition")
    else:
        context['login'] = '注销'
        context['login_URL'] = 'logout'
        return render(request, 'myreserve.html', context)


def myinfo(request):
    context = {}
    user = request.session.get('user', None)
    if user is None:
        context['login'] = '登录'
        context['login_URL'] = 'login'
        return HttpResponseRedirect("transition")
    else:
        context['login'] = '注销'
        context['login_URL'] = 'logout'
        return render(request, 'myinfo.html', context)


def transition(request):
    context = {}
    return render(request, 'transition.html', context)
