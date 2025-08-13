from django.contrib import admin
from .models import Equipment

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_available', 'owner')
    search_fields = ('name', 'description')
    list_filter = ('is_available',)

    def get_readonly_fields(self, request, obj=None):
        # Если не админ — сделать все поля только для чтения
        if not request.user.is_superuser:
            return [f.name for f in self.model._meta.fields]
        return []

    def get_fields(self, request, obj=None):
        """Ограничить видимость полей по правилам (+ и -)"""
        fields = ['name', 'description', 'is_available', 'owner']
        if request.user.is_superuser:
            fields.append('note')  # - только админ
        return fields
