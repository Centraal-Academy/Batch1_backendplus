from django.contrib import admin
from . import models
from . import apps
# Register your models here.

admin.site.register(models.Person)
admin.site.register(models.Program)
admin.site.register(models.Event)
admin.site.register(models.Meetup)
admin.site.register(models.EventPerson)