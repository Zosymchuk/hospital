from django.contrib import admin

from .models import doctor, sp, diseases

# Register your models here.
admin.site.register(doctor)
admin.site.register(sp)
admin.site.register(diseases)
