from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
  
  class Meta:
    model = Post
    fields = ('title', 'content')
    widgets = {
      'title': forms.TextInput(attrs={'required': True},)
    }
    labels = {
      'title': '제목이에요!',
    }
    help_texts = {
      'title': '제목을 적어주셔야해요!',
    }
    error_messages = {
        'title': {
            'required': '입력 좀...'
        },
    }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']