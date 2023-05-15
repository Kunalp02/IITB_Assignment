from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import Blog, BlogPost
from .serializers import BlogSerializer, BlogPostSerializer


def blog(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(user=request.user)
        print(blogs)
        return render(request, 'blog.html', context={'blogs': blogs})
    return render(request, 'blog.html')

def delete_post(request, post_id):
    if request.user.is_authenticated:
        post = BlogPost.objects.get(id=post_id, user=request.user)
        post.delete()
    return redirect('/blog/')

def delete_blog(request, blog_id):
    if request.user.is_authenticated:
        blog = get_object_or_404(Blog, id=blog_id)
        blog.delete()
    return redirect('/blog/')

def create_blog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            print(title, description)
            blog = Blog(user=request.user, title=title, description=description)
            blog.save()
            return redirect('/blog/')
        return render(request, 'create_blog.html')

def blog_posts(request, blog_id):
    if request.user.is_authenticated:
        posts = BlogPost.objects.filter(blog__id=blog_id)
        print(posts)
    return render(request, 'blog_posts.html', context={'posts': posts})

def create_post(request, blog_id):
    if request.user.is_authenticated:
        blog = get_object_or_404(Blog, id=blog_id)

        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            post = BlogPost(blog=blog, title=title, content=content)
            post.save()
            return redirect('/blog/blog_posts/' + str(blog_id))

        return render(request, 'create_post.html', context={'blog_id': blog_id})


@api_view(['GET'])
@permission_classes([IsAdminUser])
def blog_list(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def blog_list(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)
