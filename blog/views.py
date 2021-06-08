
from .forms import CommentForm, PostForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from django.utils import timezone

# Create your views here.

#메인 페이지 , 처음 들어가면 실행되는 페이지
def main(request):
    return render(request,'blog/main.html')


#글쓰기 함수, write.html과 연결되어 실행됨
def create(request):

    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid(): #값이 있으면
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('read') #저장하면 read.html불러오기
    else: #아니면
        form = PostForm
        return render(request, 'blog/write.html', {'form':form,})
        # 다시 write.html 불러옴

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
    return render(request, 'blog/read.html',{'posts':posts})
