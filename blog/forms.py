from django import forms
from .models import Post
from .models import Comment
from django.contrib.auth.decorators import login_required

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','date_posted','description','content']

class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post','name','dated','active']