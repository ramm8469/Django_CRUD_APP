from django.shortcuts import render

from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy # For redirecting
from .models import Posts
# Create your views here.

class HomePageView(ListView):
    model = Posts
    template_name = 'home.html'
    context_object_name = 'all_posts'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class PostDetailView(DetailView):
    model = Posts
    template_name = 'post_detail.html'
    # context_object_name = 'all_posts'

class PostCreateView(CreateView):
    model = Posts
    template_name = 'add_post.html'
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Posts
    template_name = 'post_edit.html'
    fields = ['title','body']

class PostDeleteView(DeleteView):
    model = Posts
    template_name = 'delete_post.html'
    success_url  = reverse_lazy('Home')
    # We use reverse_lazy as opposed to just reverse 
    # so that it won’t execute the URL
    # redirect until our view has finished deleting the blog post.


