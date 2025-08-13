from django.db import models
from people.models import Person

class Equipment(models.Model):
    name = models.CharField(max_length=255)  # +
    description = models.TextField(blank=True)  # +
    is_available = models.BooleanField(default=True)  # +
    owner = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, related_name='owned_equipment')  # +
    note = models.TextField(blank=True)  # -

    def __str__(self):
        return self.name
