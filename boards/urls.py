from django.urls import path
from boards import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),  
]
