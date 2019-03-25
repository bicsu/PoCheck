from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'attend/post_list.html',{'posts':posts})
    
    
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
        'buttons':['출석체크 확인', '오늘 RIST 식단']
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
        msg = "https://ssgfoodingplus.com/fmn101.do?goTo=todayMenu&storeCd=05600"
 
    return_dict =  JsonResponse({
            'message': {
                'text': msg
            },
            'keyboard': {
                'type':'buttons',
                'buttons':['출석체크 확인', '오늘 RIST 식단']
            }

        })
    if img_bool == False:
        return return_dict
    else : 
        pass