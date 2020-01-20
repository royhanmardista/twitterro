from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# using class base view (crud)
from django.views.generic import ListView, DetailView, CreateView, UpdateView
# implementing login mixin for class base view decorators
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



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

def about(request) :
    return render(request, "post/about.html", {'title' : 'about'})

