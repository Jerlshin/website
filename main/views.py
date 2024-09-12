# main/views.py
from django.shortcuts import render, get_object_or_404
from .models import BlogPost  # Import your BlogPost model

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def education(request):
    return render(request, 'education.html')

def publication(request):
    return render(request, 'publication.html')

def contact(request):
    return render(request, 'contact.html')

def blog_home(request):
    posts = BlogPost.objects.all()  # Fetch all blog posts
    return render(request, 'blog_home.html', {'posts': posts})

def blog_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)  # Fetch a specific blog post by ID
    return render(request, 'blog_detail.html', {'post': post})
