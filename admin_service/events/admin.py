from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'date', 'status')
    search_fields = ('name', 'description', 'place')
    list_filter = ('status',)

    def get_readonly_fields(self, request, obj=None):
        # Если не админ — сделать все поля только для чтения
        if not request.user.is_superuser:
            return [f.name for f in self.model._meta.fields]
        return []

    def get_fields(self, request, obj=None):
        """Ограничить видимость полей по правилам (+ и -)"""
        fields = ['name', 'description', 'place', 'date', 'speakers', 'status']
        if request.user.is_superuser:
            fields.extend(['guests', 'visits'])  # - только админ
        return fields
