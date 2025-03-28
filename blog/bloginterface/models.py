from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique= True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length= 200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null= True, blank=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    published = models.BooleanField(default= False)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name= 'comments')
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"