from django.contrib import admin
from starseed.models import *
import pprint
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils.html import mark_safe
admin.site.register(Person)
admin.site.register(Organization)
admin.site.register(Connection)
admin.site.register(ConnectionType)

class ProjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Project._meta.get_fields()]

admin.site.register(Project, ProjectAdmin)


class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return mark_safe(pprint.pformat(obj.get_decoded()).replace('\n', '<br>\n'))
    _session_data.allow_tags=True
    list_display = ['session_key', '_session_data', 'expire_date']
    readonly_fields = ['_session_data']
    exclude = ['session_data']
    date_hierarchy='expire_date'
admin.site.register(Session, SessionAdmin)