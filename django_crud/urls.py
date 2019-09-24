from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('boards/', include('boards.urls')), # django 기초에서 template 부분을 다룰 때 반드시 include를 설명하고 사용할 것
]
