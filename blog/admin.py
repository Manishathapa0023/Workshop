from django.contrib import admin

from .models import *

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(BloodDoner)

# Register your models here.
