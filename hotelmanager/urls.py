from django.conf.urls import url
from . import views
from . import views_control
from . import ajax_control
urlpatterns = [
    # 主页

    url(r'^$', views.index, name='index'),
    url(r'^indexpage', views.index, name='index'),
    url(r'^login', views.login),
    url(r'^sighup', views.sighup),
    url(r'^book', views.book),
    url(r'^reserve', views.reserve),
    url(r'^myreserve', views.myreserve),
    url(r'^myinfo', views.myinfo),
    url(r'^control_sighup', views_control.sighup_control),
    url(r'^control_login', views_control.login_control),
    url(r'^logout', views.loginout),
    url(r'^transition', views.transition),
    url(r'^search_room',ajax_control.search_room),

]
