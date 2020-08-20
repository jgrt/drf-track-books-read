from django.db import models
from django.utils import timezone


class Book(models.Model):
    name = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} By {}".format(self.name, self.author)

    class Meta:
        ordering = ['created']
