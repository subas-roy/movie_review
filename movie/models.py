from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)
    
    def __str__(self) -> str:
        return self.title

# class Category(models.Model):
#     name = models.CharField(max_length=20)
#     parent_category = models.ForeignKey('self', related_name='sub_category', blank=True)

class Review(models.Model):
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watchAgain = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.text