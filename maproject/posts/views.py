from django.shortcuts import render

# Create your views here.

def posts_lest(request):
    return render(request, 'posts/posts_lest.html')
