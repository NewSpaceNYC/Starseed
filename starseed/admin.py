from django.contrib import admin
from starseed.models import Person
from starseed.models import Organization
from starseed.models import Connection
from starseed.models import ConnectionType

from django.contrib.auth.models import User


admin.site.register(Person)
admin.site.register(Organization)
admin.site.register(Connection)
admin.site.register(ConnectionType)

