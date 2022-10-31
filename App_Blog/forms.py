from django import forms
from .models import Post, Comment


'''class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('anime_name','sub_name','content', 'photo','published_at','category')
        widgets = {'content': forms.Textarea(attrs={'required': True, 'cols': 80}),
                   'photo': forms.FileInput(),
                   'published_at': forms.DateInput(attrs={'type': 'date'})}'''


class FormPost(forms.Form):
    ingreso = forms.CharField(label="Leer más")


class FormComment(forms.ModelForm):
    Nombre = forms.CharField(label="Nombre de usuario", max_length=50)
    Comentario = forms.CharField(widget=forms.Textarea(attrs = {
        "class": "formulario_ms",
        "placeholder": "Escribe tu mensaje",
    }))