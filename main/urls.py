# portfolio/urls.py
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('education/', views.education, name='education'),
    path('publication/', views.publication, name='publication'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog_home, name='blog_home'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),  # New URL pattern for blog detail
]
