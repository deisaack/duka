from __future__ import unicode_literals
from django.contrib import admin
from authtools.admin import NamedUserAdmin
from django.contrib.auth import get_user_model
from duka.profiles.models import DataCollector

User = get_user_model()


class DataCollectorInline(admin.StackedInline):
    model = DataCollector

class NewUserAdmin(NamedUserAdmin):
    inlines = [DataCollectorInline]
    list_display_links = ('email', 'name',)
    list_display = ('is_active', 'email', 'name',
                    'is_superuser', 'is_staff',)


admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)
