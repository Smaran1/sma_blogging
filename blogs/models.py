from django.db import models
from django.conf import settings
from django.utils import timezone
from django.apps import AppConfig
# Create your models here.
#settings.configure() 
class Post (models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    comments = models.TextField()
    
    

   
