"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
import blog.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.main, name='main'), #제일 먼저 보이는 페이지
    path('read/',blog.views.read, name='read'),
    path('detail/<str:id>',blog.views.detail, name ='detail'),
    path('write/create/', blog.views.create, name='create'), #write 페이지에 create함수를 연결하여 보여줌
    path('edit/<str:id>', blog.views.edit, name='edit'), #string 타입 id를 받아옴
    path('delete/<str:id>/', blog.views.delete, name = 'delete'),  #string 타입 id를 받아옴
    path('blog/hashtag/', blog.views.hashtagform, name='hashtag'),
    path('blog/<int:hashtag_id>/search/',blog.views.search,name='search'),
    path('account/',include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
