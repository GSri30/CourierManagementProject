from django.contrib import admin
from .models import EmailMapping, MobileNumberMapping

# Register your models here.
admin.site.register(EmailMapping)
admin.site.register(MobileNumberMapping)