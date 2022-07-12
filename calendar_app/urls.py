"""djangoCalendar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from calendar_app import views
from .views import EventCreateView, EventDetailView, EventDeleteView, EventUpdateView

urlpatterns = [
    path('', views.home, name='page-home'),
    path('event/new/', EventCreateView.as_view(), name='page-new'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='page-detail'),
    path('event/<int:pk>/delete', EventDeleteView.as_view(), name='page-delete'),
    path('event/<int:pk>/update', EventUpdateView.as_view(), name='page-update'),
]
