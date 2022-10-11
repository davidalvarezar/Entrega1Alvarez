from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormMensajes(forms.Form):
    mensaje = forms.CharField(widget=forms.Textarea (attrs = {"placeholder": "Escribe tu mensaje" }))
        
       
        
        
        

