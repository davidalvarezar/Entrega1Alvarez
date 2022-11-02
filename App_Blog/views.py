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
    new_comment = None
    if request.method == 'POST':
        #comment_form = FormComment(request.POST)
        if comment_form.is_valid():
            #Se crea el comentario pero no se guarda en la base de datos
            new_comment = comment_form.save(commit=False)
            #se asigna el comentario al post correspondiente
            new_comment.post = post
            #ahora si se guarda el form en la db
            new_comment.save()
        
    else:
        comment_form = FormComment()

    return render(request, 'post_detail.html', {'post': post,'new_comment': new_comment,'comment_form': comment_form})



    
