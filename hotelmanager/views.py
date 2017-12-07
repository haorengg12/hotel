from django.shortcuts import render

# Create your views here.


def index(request):
    context = { }
    context['img1'] = 'img/room/1.jpg'
    context['img2'] = 'img/room/2.jpg'
    context['img3'] = 'img/room/3.jpg'
    context['img4'] = 'img/room/4.jpg'
    context['img5'] = 'img/room/5.jpg'
    context['img6'] = 'img/room/6.jpg'

    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')


def sighup(request):
    return render(request, 'sighup.html')


def book(request):
    context = {}
    return render(request, 'bookpage.html')


def reserve(request):
    return render(request, 'reserve.html')


def myreserve(request):
    return render(request, 'myreserve.html')


def myinfo(request):
    return render(request, 'myinfo.html')
