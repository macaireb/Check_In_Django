from django.contrib import admin
from .models import Resident, Counselor, Punch

# Register your models here.

admin.site.register(Resident)
admin.site.register(Counselor)
admin.site.register(Punch)
