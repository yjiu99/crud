from django import forms
from django.db.models import fields
from .models import Comment, Post, Hashtag

# model Instance를 생성,수정,제거 하는 Form을 작성, 필드에는 'title', 'writer', 'body' 저장
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'writer', 'body', 'hashtags', 'image']

# CommentForm 추가
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

# HashtagForm 추가
class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']