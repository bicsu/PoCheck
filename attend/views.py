from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
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


# Create your views here.
# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'attend/post_list.html',{'posts':posts})
    
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'attend/post_detail.html', {'post': post})    
    
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'attend/post_edit.html', {'form': form})

def check(request):
    return render(request, 'attend/check.html')



    
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'attend/post_edit.html', {'form': form})
    
##### kakao

def keyboard(request):
 
    return JsonResponse({
        'type':'buttons',
        'buttons':['출석체크 확인', '오늘 RIST 식단','시간표']
    })

@csrf_exempt
def message(request):
    img_bool = False
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']
    
    if datacontent =='출석체크 확인':
        
        msg = '이 기능은 아직;;'
    elif datacontent == '오늘 RIST 식단':
        
        url = 'https://ssgfoodingplus.com/fmn101.do?goTo=todayMenuJson'
        yearmonth = datetime.datetime.now().strftime("%Y-%m-")
        now = datetime.datetime.now()
        month = now.month
        day = now.day
        r = datetime.datetime.today().weekday()
        hour = datetime.datetime.now().hour
        if hour>=14:
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
        for i in range(0,len(res['result'])):
            if res['result'][i]['meal_type_nm']=="조식":
                breakfast+=res['result'][i]['if_menu_nm']+"\n"
            elif res['result'][i]['meal_type_nm']=="중식":
                lunch+=res['result'][i]['if_menu_nm']+"\n"
            elif res['result'][i]['meal_type_nm']=="석식":
                dinner+=res['result'][i]['if_menu_nm']+"\n"
        msg ="RIST식당/{0}요일\n-------조식-------\n{1}\n-------중식-------\n{2}\n-------석식-------\n{3}\n".format(days[r],breakfast,lunch,dinner)
        
        
    elif datacontent =='시간표':
        img_bool = True
        msg = 'B반의 시간표'
        url = 'static/css/images/timetable.jpg'
        
 
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
                'width':480,
                'height':640
                }
            
        },
        'keyboard': {
            'type':'buttons',
            'buttons':['출석체크 확인', '오늘 RIST 식단','시간표']
        }

    })
    if img_bool :
        return return_img_dict
    else : 
        return return_dict