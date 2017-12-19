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
    url(r'^search_room', ajax_control.search_room),
    url(r'^check_reserve', views_control.check_reserve),
    url(r'^update_myinfo', ajax_control.myinfo_update),
    url(r'^all_check',ajax_control.all_check),
    url(r'^staff',views.staff),
    url(r'^cus_search', ajax_control.cus_search),
    url(r'^all_reserve',ajax_control.all_reserve),
    url(r'^res_reserve',ajax_control.res_reserve),
    url(r'^insert_check', ajax_control.insert_check),
    url(r'^get_room_by_id', ajax_control.get_room_by_id),
    url(r'^get_room_by_date', ajax_control.get_room_by_date),
    url(r'^add_room', ajax_control.add_room),
    url(r'^delete_room', ajax_control.delete_room),
    url(r'^delete_check', ajax_control.delete_check),
]
