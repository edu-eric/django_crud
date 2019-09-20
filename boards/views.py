from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):

    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):

    title = request.POST.get('title')
    content = request.POST.get('content')
    Post.objects.create(title=title, content=content)
    return render(request, 'create.html')