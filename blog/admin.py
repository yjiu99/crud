from django.contrib import admin
from .models import Hashtag, Post, Comment

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Hashtag)