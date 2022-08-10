from django.contrib import admin

from apps.service.models import Invoice, Phone

admin.site.register(Phone)
admin.site.register(Invoice)
