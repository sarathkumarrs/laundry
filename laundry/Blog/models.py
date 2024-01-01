from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='blog_images/')
    date = models.DateField()
    title = models.CharField(max_length=200)
    content = RichTextField()

    def __str__(self):
        return self.title