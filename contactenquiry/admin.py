from django.contrib import admin
from contactenquiry.models import contactenquiry

class ConatctAdmin(admin.ModelAdmin):
    list_display = ('name','email','message')
    
admin.site.register(contactenquiry,ConatctAdmin)

# Register your models here.
