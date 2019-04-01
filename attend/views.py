from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Check
from django.utils import timezone
from .forms import PostForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import datetime
from bs4 import BeautifulSoup
import random
import os
import re
import requests
# tend_recvup_attend
from . import attend_recv

def home(request):
    return render(request, 'attend/home.html')

def schedule(request):
    return render(request, 'attend/photos.html')

def calendar(request):
    return render(request, 'attend/tables.html', {})

def attendance(request):
    attend_dict = attend_recv.update_attend()
    pic_ex = []
    for x in attend_dict:
        tmp = x + '.jpg'
        if os.path.isfile('/home/bicsu/PoCheck/attend/static/img/people/'+tmp):
            pic_ex.append(1)
        else:
            pic_ex.append(0)
    Check.objects.all().delete()
    for k, i in enumerate(attend_dict) :
        Check.objects.create(name = i, checking=int(attend_dict[i][0]), time =attend_dict[i][1], pic = pic_ex[k])
    checks = Check.objects.all()
    length = len(Check.objects.all())
    
    return render(request, 'attend/attendance.html',  {'checks':checks, 'len':length })

def attend_list(request):
    attend_dict = attend_recv.update_attend()

    Check.objects.all().delete()
    for k, i in enumerate(attend_dict) :
        Check.objects.create(name = i, checking=int(attend_dict[i][0]), time =attend_dict[i][1])
    checks = Check.objects.all()
    length = len(Check.objects.all())
    
    return render(request, 'attend/attend_list.html',  {'checks':checks, 'len':length })
    
    
#DON'T TOUCH!
##kakao ####################################################################################################
##kakao ####################################################################################################
##kakao ####################################################################################################
##kakao ####################################################################################################
def keyboard(request):
 
    return JsonResponse({
        'type':'buttons',
        'buttons':['출석체크 확인', '오늘 RIST 식단','시간표']
    })

@csrf_exempt
def message(request):
    img_bool = False
    text_bool = False
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']
    msg = 'ㅎㅎ'
    url = 'ㅎㅎ'
    attend_dict = attend_recv.update_attend()
    for_name = list(attend_dict.keys())
    for_other = ['출석체크 확인', '오늘 RIST 식단','시간표']
    
    if datacontent in for_name :
        text_bool = True
        students = Check.objects.get(name=datacontent)
        if students.checking == 1:
            msg = '출석이 완료됐습니다.'
        else :
            msg = '출석을 안하셨네요 :( \n 출석해주세요.'
    elif datacontent in for_other :
        if datacontent =='출석체크 확인':
            text_bool = True
            msg = '이름을 입력해주세요(ex. 홍길동)'
            
        elif datacontent == '오늘 RIST 식단':
            url = 'https://ssgfoodingplus.com/fmn101.do?goTo=todayMenuJson'
            yearmonth = datetime.datetime.now().strftime("%Y-%m-")
            now = datetime.datetime.now()
            month = now.month
            day = now.day
            r = datetime.datetime.today().weekday()
            hour = datetime.datetime.now().hour
            if hour>=18:
                if r==6:
                    r=0
                else :
                    r+=1
                if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
                    if day==31:
                        month+=1
                        day=1
                    else:
                        day+=1
                else:
                    if day==30:
                        month+=1
                        day=1
                    else :
                        day+=1
            
            today = yearmonth+str("%02d"%day)
            days=["월","화","수","목","금","토","일"]
            payloads = {"storeCd": "05600", "cafeCd": "01", "menuDate": today}
            res = requests.post(url, data= payloads).json()
            breakfast=""
            lunch=""
            dinner=""
            dinner_b=""
            for i in range(0,len(res['result'])):
                if res['result'][i]['meal_type_nm']=="조식":
                    breakfast+=res['result'][i]['if_menu_nm']+"\n"
                elif res['result'][i]['meal_type_nm']=="중식":
                    lunch+=res['result'][i]['if_menu_nm']+"\n"
                elif res['result'][i]['meal_type_nm']=="석식":
                    if res['result'][i]['dinner_type_nm']=="일반식(한식)":
                        dinner+=res['result'][i]['if_menu_nm']+"\n"
                    elif res['result'][i]['dinner_type_nm']=="일반식(양식)":
                        dinner_b+=res['result'][i]['if_menu_nm']+"\n"
                    
            if r == 5 or r == 6 :
                msg = '주말입니다;;\nRIST식당은 밥을 주지 않습니다.'
            else : 
                msg ="RIST식당/{0}요일\n-------조식-------\n{1}\n-------중식-------\n{2}\n-------석식A-------\n{3}\n-------석식B-------\n{4}\n".format(days[r],breakfast,lunch,dinner,dinner_b)
            
        elif datacontent =='시간표':
            img_bool = True
            msg = 'http://bicsu.pythonanywhere.com/schedule'
            url = 'http://bicsu.pythonanywhere.com/static/images/schedule_B.jpg'
    else :
        msg = '등록된 학생이 아닙니다. 수현쌤에게 문의해주세요 :)'
    return_dict =  JsonResponse({
            'message': {
                'text': msg
            },
            'keyboard': {
                'type':'buttons',
                'buttons':['출석체크 확인', '오늘 RIST 식단','시간표']
            }
        })
    return_img_dict =  JsonResponse({
        'message': {
            'text': msg,
            'photo':{
                'url':url,
                'width':1024,
                'height':768
                }
            
        },
        'keyboard': {
            'type':'buttons',
            'buttons':['출석체크 확인', '오늘 RIST 식단','시간표']
        }})
    return_text_dict =  JsonResponse({
            'message': {
                'text': msg
            },
            'keyboard': {
                'type':'text'}
                                    })
    
    if img_bool :
        return return_img_dict
    elif text_bool :
        return return_text_dict
    else : 
        return return_dict
        