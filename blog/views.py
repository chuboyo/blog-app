from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BListView(ListView):
   model = Post
   template_name = 'home.html'

class BDetailView(DetailView):
   model = Post
   template_name = 'post_detail.html'

class BCreateView(CreateView):
   model = Post
   template_name = 'post_new.html'
   fields = ['title', 'author', 'body']

class BUpdateView(UpdateView):
   model = Post
   template_name = 'post_edit.html'
   fields = ['title', 'body']

class BDeleteView(DeleteView):
   model = Post
   template_name = 'post_delete.html'
   success_url = reverse_lazy('home')


