from django.urls import path
from boards import views

app_name = 'boards'

urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('detail/<int:board_id>/', views.detail, name="detail"),
    path('delete/<int:board_id>/', views.delete, name="delete"),
    path('edit/<int:board_id>/', views.edit, name="edit"),
    path('update/<int:board_id>/', views.update, name="update"),

    # 댓글 관련 URL
    path('comment/create/<int:board_id>/', views.create_comment, name="create_comment"),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name="delete_comment"),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name="edit_comment"),
    path('comment/update/<int:comment_id>/', views.update_comment, name="update_comment"),
]
