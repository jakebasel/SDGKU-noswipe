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
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = "event_delete.html"
    success_url = reverse_lazy('Events')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TicketDetailView(CreateView):
    model = Ticket
    template_name = "ticket_cart.html"
    fields = ['ticket_holder_first_name', 'ticket_holder_email', 'event_id']

