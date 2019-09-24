from django.urls import path
from boards import views

app_name = 'boards'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('/<int:board_id>/', views.detail, name='detail'),
    path('/<int:board_id>/delete/', views.delete, name='delete'),
    path('/<int:board_id>/edit/', views.edit, name='edit'),
    path('/<int:board_id>/update/', views.update, name='update'),
    
    # 댓글 관련 URL
    path('comment/<int:board_id>/', views.create_comment, name='create_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/update/', views.update_comment, name='update_comment'),
]
