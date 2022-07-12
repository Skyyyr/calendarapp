from django.shortcuts import render
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from calendar_app.models import Event


def home(request):
    events = {
        'events': Event.objects.all()
    }
    return render(request, 'calendar_app/home.html', events)


class EventCreateView(CreateView):
    model = Event
    fields = ['name', 'description', 'starts_at', 'ends_at']


class EventDetailView(DetailView):
    model = Event


class EventDeleteView(DeleteView):
    model = Event
    success_url = '/'


class EventUpdateView(UpdateView):
    model = Event
    fields = ['name', 'description', 'starts_at', 'ends_at']
