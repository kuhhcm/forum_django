from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Thread, Post, Comment

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ThreadCreateForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content']
        

class ThreadUpdateForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content']
        
        
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        
class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] 
        
        