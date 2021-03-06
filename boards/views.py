from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def index(request):

    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)

def new(request):
    
    context = {
        'PostForm': PostForm,
    }
    return render(request, 'new.html', context)

def create(request):

    new_post = PostForm(request.POST)
    if new_post.is_valid():
        title = new_post.cleaned_data.get('title')
        content = new_post.cleaned_data.get('content')
        Post.objects.create(title=title, content=content)
        return render(request, 'create.html')
    else:
        return redirect('/boards/')

def detail(request, board_id):
    
    post = Post.objects.get(id=board_id)
    context = {
        'post': post,
    }
    return render(request, 'detail.html', context)

def delete(request, board_id):

    post = Post.objects.get(id=board_id)
    post.delete()
    return render(request, 'delete.html')

def edit(request, board_id):

    post = Post.objects.get(id=board_id)
    context = {
        'post': post,
    }
    return render(request, 'edit.html', context)

def update(request, board_id):

    post = Post.objects.get(id=board_id)
    new_title = request.POST.get('title')
    new_content = request.POST.get('content')
    post.title = new_title
    post.content = new_content
    post.save()
    return render(request, 'update.html')

def create_comment(request, board_id):
    
    post = Post.objects.get(id=board_id)
    name = request.POST.get('name')
    content = request.POST.get('content')
    new_comment = Comment.objects.create(name=name, content=content, post=post)
    return redirect('/boards/')

def delete_comment(request, comment_id):
    
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('/boards/')

def edit_comment(request, comment_id):

    comment = Comment.objects.get(id=comment_id)
    return render(request, 'edit_comment.html', {'comment': comment})

def update_comment(request, comment_id):
    
    comment = Comment.objects.get(id=comment_id)
    new_name = request.POST.get('name')
    new_content = request.POST.get('content')
    comment.name = new_name
    comment.content = new_content
    comment.save()
    return redirect('/boards/')

