from django.contrib import admin
from starseed.models import *

from django.contrib.auth.models import User


admin.site.register(Person)
admin.site.register(Organization)
admin.site.register(Connection)
admin.site.register(ConnectionType)

class ProjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Project._meta.get_fields()]

admin.site.register(Project, ProjectAdmin)

