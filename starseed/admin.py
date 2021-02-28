from django.contrib import admin
from starseed.models import *

from django.contrib.auth.models import User


admin.site.register(Person)
admin.site.register(Organization)
admin.site.register(Connection)
admin.site.register(ConnectionType)
admin.site.register(Project)

