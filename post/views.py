from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# using class base view (crud)
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# implementing login mixin for class base view decorators
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


# Create your views here.
def home(request) :
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "post/home.html", context)

class PostListView(ListView) :
    model = Post
    template_name = 'post/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView) :
    model = Post
    template_name = 'post/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView) :
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView) :
    model = Post
    fields = ['title', 'content']

# overiding the author before save
    def form_valid(self, form) :
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView) :
    model = Post
    fields = ['title', 'content']

# overiding the author before save
    def form_valid(self, form) :
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # implementing authorization
    def test_func(self) :
        post = self.get_object()
        if (self.request.user == post.author) :
            return True
        else :
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView) :
    model = Post
    success_url = '/'
    
    # implementing authorization
    def test_func(self) :
        post = self.get_object()
        if (self.request.user == post.author) :
            return True
        else :
            return False

def about(request) :
    return render(request, "post/about.html", {'title' : 'about'})

