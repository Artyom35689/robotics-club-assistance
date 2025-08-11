from django.db import models

class Event(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Запланировано'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершено'),
    ]

    name = models.CharField(max_length=255)  # +
    description = models.TextField(blank=True)  # +
    place = models.CharField(max_length=255)  # +
    date = models.CharField(max_length=255)  # +
    speakers = models.ManyToManyField('people.Person', related_name='speaking_events', blank=True)  # +
    guests = models.ManyToManyField('people.Person', related_name='guest_events', blank=True)  # -
    visits = models.ManyToManyField('people.Person', related_name='visited_events', blank=True)  # -
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)  # +

    def __str__(self):
        return self.name
