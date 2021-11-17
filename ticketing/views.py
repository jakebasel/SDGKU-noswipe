from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.http import request
from django.urls.base import reverse
from django.views.generic import ListView, DetailView
from .models import Event, Ticket
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .forms import TicketForm

class EventListView(ListView):
    model = Event
    template_name = "event_list.html"

class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = "event_detail.html"

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    template_name = "event_create.html"
    fields = ['author', 'title','body','image','date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    template_name = "event_update.html"
    fields = ['title', 'body', 'image','date']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = "event_delete.html"
    success_url = reverse_lazy('event_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

def ticket_create_view(request, pk, methods=['GET', 'POST']):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_ticket = Ticket(ticket_holder_first_name = data["ticket_holder_first_name"],ticket_holder_last_name = data["ticket_holder_last_name"], ticket_holder_email=data["ticket_holder_email"], event_id=data["event_id"])
            new_ticket.save()
            event = Event.objects.get(id=pk)
            event.current_attendee_count += 1
            event.remaining_capacity = event.max_attendee - event.current_attendee_count
            event.save()
            return redirect('/ticketing')
    else:
        form = TicketForm()
        return render(request, 'ticket_cart.html', context={"form":form})

