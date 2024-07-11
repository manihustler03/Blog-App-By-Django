from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=50)


    def __str__(self):
        return self.title

