from django.urls import path
from . import views


urlpatterns = [
    path('blog/', views.blog, name="blog"),
    path('blog/delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('blog/delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('blog/blog_posts/<int:blog_id>/', views.blog_posts, name='blog_posts'),
    path('blog/create_blog/', views.create_blog, name='create_blog'),
    path('blog/create_post/<int:blog_id>/', views.create_post, name='create_post'),
    path('api/blogs/', views.blog_list, name='blog_list'),
    path('api/create_blog/', views.create_blog, name='create_blog'),
]
