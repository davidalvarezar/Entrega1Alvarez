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
    if request.method == "POST":
        comment_form = FormComment(request.POST)
        if comment_form.is_valid():
            nombre = comment_form.cleaned_data.get('nombre')
            comentario = comment_form.cleaned_data.get('comentario')
        
            return render (request, "principal_blog.html", {"mensaje": "¡Comentario enviado!"})
            
    else:
        comment_form = FormComment()

    return render(request, 'post_detail.html', {'post': post,'comment_form': comment_form})
    



    
