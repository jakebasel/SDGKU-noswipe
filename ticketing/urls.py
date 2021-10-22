from django.urls import path
from .views import (TicketDetailView, 
EventDeleteView, 
EventListView, 
EventCreateView, 
EventUpdateView,
EventDetailView)

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('new/', EventCreateView.as_view(), name='event_new'),
    path('<int:pk>/update', EventUpdateView.as_view(), name='event_update'),
    path('<int:pk>/delete', EventDeleteView.as_view(), name='event_delete'),
    path('<int:pk>/purchase', TicketDetailView.as_view(), name='ticket_detail'),
]