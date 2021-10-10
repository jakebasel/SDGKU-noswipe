from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    #date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])