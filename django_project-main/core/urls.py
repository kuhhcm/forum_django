from django.contrib import admin
from django.urls import path
from app.views import home, UserRegistrationView, UserLoginView, user_logout, ThreadListView, ThreadDetailView,ThreadCreateView, ThreadUpdateView, ThreadDeleteView, PostListView, post_detail, PostCreateView, PostUpdateView, PostDeleteView, my_profile



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='home'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('threads/', ThreadListView.as_view(), name='thread_list'),
    path('threads/detail/<int:pk>/', ThreadDetailView.as_view(), name='thread_detail'),
    path('threads/create/', ThreadCreateView.as_view(), name='thread_create'),
    path('threads/<int:pk>/update/', ThreadUpdateView.as_view(), name='thread_update'),
    path('threads/<int:pk>/delete/', ThreadDeleteView.as_view(), name='thread_delete'),
    path('posts/detail/<int:post_id>/', post_detail, name='post_detail'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('my_profile/', my_profile, name='my_profile'),
]
