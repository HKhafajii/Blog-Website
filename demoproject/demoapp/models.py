from django.db import models
from unicodedata import name 

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' : ' + self.email + ' : ' + self.username
    
class Post(models.Model):
    Title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='users')



    

