from django.urls import path
from boards import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('detail/<int:board_id>/', views.detail),
    path('delete/<int:board_id>/', views.delete),
    path('edit/<int:board_id>/', views.edit),
    path('update/<int:board_id>/', views.update),

    # 댓글 관련 URL
    path('comment/create/<int:board_id>/', views.create_comment),
    path('comment/delete/<int:comment_id>/', views.delete_comment),
]
