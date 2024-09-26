from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    return render(request, 'home.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post': post})
