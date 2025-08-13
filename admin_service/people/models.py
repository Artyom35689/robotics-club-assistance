from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    ACCESS_LEVELS = [
        ('admin', 'Администратор'),
        ('user', 'Пользователь'),
    ]

    email = models.EmailField(unique=True)  # +
    full_name = models.CharField(max_length=255)  # +
    telegram_alias = models.CharField(max_length=255, blank=True)  # +
    equipment = models.ManyToManyField('equipment.Equipment', blank=True, related_name='users_equipment')
    access_level = models.CharField(max_length=10, choices=ACCESS_LEVELS)  # +
    about = models.TextField(blank=True)  # +
    note = models.TextField(blank=True)  # -
    
    def __str__(self):
        return self.full_name
