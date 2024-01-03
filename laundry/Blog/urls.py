from django.contrib import admin
from django.urls import path
from . import views

app_name='Blog'

urlpatterns = [

    path('Blog/blog/',views.blog,name='blog'),
    path('Blog/blog_details/<int:pk>/',views.blog_details,name='blog_details'),
    path('Blog/blog_details/',views.blog_details,name='blog_details'),
    path('post_comment/<int:pk>/', views.post_comment, name='post_comment'),
    path('search/', views.search_view, name='search_results'),
    path('blogs_by_category/<int:category_id>/', views.blogs_by_category, name='blogs_by_category'),

]
