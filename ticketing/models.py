from django.db import models
from django.core.validators import validate_slug
from django import forms
from django.contrib.auth import get_user_model
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField()
    price = models.FloatField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='static/images/')
    current_attendee_count = models.BigIntegerField()
    max_attendee = models.BigIntegerField()
    remaining_capacity = models.BigIntegerField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])

class Ticket(models.Model):
    ticket_holder_first_name = models.CharField(validators=[validate_slug], max_length=25)
    ticket_holder_last_name = models.CharField(validators=[validate_slug], max_length=25)
    ticket_holder_email = models.EmailField(max_length=35)
    event_id = models.ForeignKey(
        Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.ticket_holder_email

    def get_absolute_url(self):
        return reverse('ticket_detail', args=[str(self.id)])

    