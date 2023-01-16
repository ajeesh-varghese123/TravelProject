from django.contrib import admin

from . models import Places
from . models import Clients

# Register your models here.

admin.site.register(Places)
admin.site.register(Clients)
