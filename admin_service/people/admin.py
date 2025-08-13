from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'telegram_alias', 'access_level')
    search_fields = ('email', 'full_name', 'telegram_alias')
    list_filter = ('access_level',)

    def get_readonly_fields(self, request, obj=None):
        """Ограничения редактирования полей"""
        if request.user.is_superuser:
            return []
        # Обычные пользователи могут только смотреть поля с '+'
        return [f.name for f in self.model._meta.fields]
