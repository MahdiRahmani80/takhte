from django.shortcuts import render , get_object_or_404
from .models import Post 

def index(request):
    post = Post.objects.all

    dic = {
        'post' : post , 
    }

    return render(request, "index.html", dic)