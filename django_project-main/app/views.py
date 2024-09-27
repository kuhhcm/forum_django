from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, ThreadCreateForm, ThreadUpdateForm, PostCreateForm, PostUpdateForm, CommentForm
from django.contrib.auth.views import LoginView
from .models import Thread, Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')



# User views
class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration.html'
    
class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('home')
    redirect_authenticated_user = True
    
@login_required
def user_logout(request):
    logout(request=request)
    return render(request=request, template_name='home.html')
    

# Thread views
class ThreadListView(ListView):
    model = Thread
    template_name = 'thread_list.html'
    context_object_name = 'threads'
    
class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'thread_detail.html'
    context_object_name = 'thread'
    
class ThreadCreateView(CreateView):
    model = Thread
    form_class = ThreadCreateForm
    template_name = 'thread_create.html'
    success_url = reverse_lazy('thread_list')
    
class ThreadUpdateView(UpdateView):
    model = Thread
    form_class = ThreadUpdateForm
    template_name = 'thread_update.html'
    success_url = reverse_lazy('thread_list')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator=self.request.user)
    
class ThreadDeleteView(DeleteView):
    model = Thread
    template_name = 'thread_delete.html'
    success_url = reverse_lazy('thread_list')
    context_object_name = 'thread'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator=self.request.user)
    
    

# Post views
class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    
@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})
    
class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('home')
    login_url = 'login'
        
class PostUpdateView(LoginRequiredMixin ,UpdateView):
    model = Post
    template_name = 'post_update.html'
    success_url = reverse_lazy('home')
    form_class = PostUpdateForm
    login_url = 'login'
    
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(creator=self.request.user)

class PostDeleteView(LoginRequiredMixin ,DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'post'
    login_url = 'login'
    
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(creator=self.request.user)
    

def my_profile(request):
    return render(request, 'my_profile.html')