
from .forms import CommentForm, PostForm, HashtagForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Hashtag
from django.utils import timezone

# Create your views here.

#메인 페이지 , 처음 들어가면 실행되는 페이지
def main(request):
    return render(request,'blog/main.html')


#글쓰기 함수, write.html과 연결되어 실행됨
def create(request):

    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid(): #값이 있으면
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('read') #저장하면 read.html불러오기
    else: #아니면
        form = PostForm
        return render(request, 'blog/write.html', {'form':form,})
        # 다시 write.html 불러옴

def blogform(request, blog=None):
    if request.method == 'POST':
        form = PostForm(request.POST, instance=blog)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.datetime.now()
            post.save()
            form.save_m2m()
            return redirect('read')
    else:
        form = PostForm(instance=blog)
        return render(request, 'blog/write.html', {'form':form})

# 수정 페이지 
def edit(request,id):
    post = get_object_or_404(Post,id=id) #객체(값) 아니면 404에러 불러옴
    if request.method =='POST':
        form = PostForm(request.POST, isinstance=post)
        if form.is_valid(): #값이 있으면
            form.save(commit=False)
            form.save()
            return redirect('read') #저장 후 read.html로

    else: #아니면
        form = PostForm(instance=post)
        return render(request,'blog/edit.html',{'form':form})
        #다시 수정 페이지로 돌아옴

# 삭제하기 함수
def delete(request,id):
    post = get_object_or_404(Post, id = id)
    post.delete() #삭제 후 
    return redirect('read')
    #read.html을 불러 전체 보이기



#디테일 페이지, 삭제하기, 수정하기 같이 있음
def detail(request,id):
    post = get_object_or_404(Post,id=id)
    if request.method =="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('detail',id)
    else:
        form=CommentForm()
        return render(request, 'blog/detail.html',{'post':post, 'form':form})

# 모든 글쓴 것들을 읽어오는 페이지 
def read(request):
    posts = Post.objects
    hashtags = Hashtag.objects
    return render(request, 'blog/read.html',{'posts':posts, 'hashtags':hashtags})


#해쉬 태그 함수
def hashtagform(request, hashtag=None):
    if request.method == 'POST':
        form = HashtagForm(request.POST, instance=hashtag)
        if form.is_valid():
            hashtag = form.save(commit=False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message = "이미 존재하는 해시 태그 입니다. "
                return render(request, 'blog/hashtag.html', {'form':form, "error_message":error_message})
            else:
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
            return redirect('read')
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'blog/hashtag.html', {'form':form})

def search(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_id)
    return render(request, 'search.html', {'hashtag':hashtag})