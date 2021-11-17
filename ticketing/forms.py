from django import forms
from .models import Event, Ticket

class PostForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('image', 'body')

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_holder_first_name', 'ticket_holder_last_name', 'ticket_holder_email', 'event_id']
        

class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['author', 'title','body','image','date', 'price', 'current_attendee_count', 'max_attendee', 'remaining_capacity']
        widgets = {
            'date': DateTimeInput(),
        }