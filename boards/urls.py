from django.urls import path
from boards import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('detail/<int:board_id>/', views.detail),
    path('delete/<int:board_id>/', views.delete),  
]
