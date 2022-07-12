from django.db import models
from django.urls import reverse
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    starts_at = models.DateTimeField(default=timezone.now)
    ends_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('page-detail', kwargs={'pk': self.pk})
