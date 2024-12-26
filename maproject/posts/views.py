from django.shortcuts import render
from .models import Post
# Create your views here.

def posts_lest(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_lest.html', {'posts': posts})


