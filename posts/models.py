from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):  # Inherits from models.Model
    title = models.CharField(max_length=128)    # CharField is for short text with a limit
    subtitle = models.CharField(max_length=256)
    body = models.TextField()   # TextField is for longer text without a limit
    created_on = models.DateTimeField(auto_now_add=True)    # auto_now_add=True sets the field to now when the object is first created.
    def __str__(self):  # __str__ method is the default human-readable representation of the object.
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
