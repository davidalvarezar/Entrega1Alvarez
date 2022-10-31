from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import*
from App_Blog.forms import*

# Create your views here.

@login_required
def posts(request):
    return render (request, "principal_blog.html")



def post_detail(request):
    
    post = Post.objects.all()

    return render(request, 'post_detail.html', {'post': post})