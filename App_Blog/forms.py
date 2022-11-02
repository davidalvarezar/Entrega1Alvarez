from django import forms
from .models import*



class FormComment(forms.Form):
        nombre = forms.CharField(label="Nombre de usuario", max_length=50)
        comentario = forms.CharField(widget=forms.Textarea(attrs = {
        "class": "formulario_ms",
        "placeholder": "Escribe tu mensaje",
    }))