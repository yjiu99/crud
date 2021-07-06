from typing import Text
from django.db import models
from django.conf import settings


# 모델을 객체로 받아 DB 연결
class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    writer = models.CharField( max_length=15, default='닉네임을 입력해주세요')
    body = models.TextField()
    hashtags = models.ManyToManyField('Hashtag',blank=True)
    image = models.ImageField(upload_to='images/', blank = True)

    def __str__(self):
        return self.title

#댓글 모델
class Comment(models.Model):
    def __str__(self):
        return self.text
    
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=50)

#해쉬테그 모델
class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name