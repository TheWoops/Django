from django import forms
from .models import Post # load the defined Post-model

class PostForm(forms.ModelForm): # tell Django that PostForm is a Django-Form

    class Meta:
         model = Post # define which model shall be used to create the form
         fields = ('title', 'text',) # define fields of the form