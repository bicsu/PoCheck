from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('attendance', views.attendance, name='attendance'),
    path('keyboard/',views.keyboard, name='keyboard'),
    path('message', views.message, name='message'),
    path('schedule', views.schedule, name='schedule'),
    path('attend_list', views.attend_list, name='attend_list'),
    ]
    # path('attendance', views.attendance, name='attendance'),
    # url(r'^index/$', views.index, name='index'),
    # path('chulcheck', views.chul_check, name='chulcheck'),
    #path('templete',views.templete,name='templete'),
    # path('post/<int:pk>', views.post_detail, name='post_detail'),
    # path('post/new', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name = 'post_edit'),