from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='static/images/')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])