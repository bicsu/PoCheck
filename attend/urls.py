from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.check, name='check'),
    # path('post/<int:pk>', views.post_detail, name='post_detail'),
    # path('post/new', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name = 'post_edit'),
    path('keyboard/',views.keyboard, name='keyboard'),
    path('message', views.message, name='message'),
    path('schedule', views.schedule, name='schedule'),
    path('calendar',views.calendar,name='calendar'),
    url(r'^index/$', views.index, name='index'),
    #path('templete',views.templete,name='templete'),
    path('chulcheck', views.chul_check, name='chulcheck'),
    ]