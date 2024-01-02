from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField(upload_to='author_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='blog_images/')
    date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=200)
    content = RichTextField()
    categories = models.ManyToManyField(Category)


    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.blog.title}'    