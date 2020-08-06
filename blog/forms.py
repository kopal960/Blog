from django import forms
from .models import Post

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','date_posted','description','content']