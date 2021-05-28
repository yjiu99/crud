
from .forms import PostForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from django.utils import timezone

# Create your views here.

#메인 페이지
def main(request):
    return render(request,'blog/main.html')

#글쓰기페이지

#글쓰기 함수
def create(request):

    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('read')
    else:
        form = PostForm
        return render(request, 'blog/write.html', {'form':form,})



def edit(request,id):
    post = get_object_or_404(Post,id=id)
    if request.method =='POST':
        form = PostForm(request.POST, isinstance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('read')

    else:
        form = PostForm(instance=post)
        return render(request,'blog/edit.html',{'form':form})


def delete(request,id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('read')


#디테일 페이지
def detail(request,id):
    post = get_object_or_404(Post,id=id)
    return render(request, 'blog/detail.html',{'post':post})


def read(request):
    posts = Post.objects
    return render(request, 'blog/read.html',{'posts':posts})
