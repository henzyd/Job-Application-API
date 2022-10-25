from django.contrib import admin
from .models import JobAdvert

# Register your models here.

class JobAdvertDisplay(admin.ModelAdmin):
    list_display = ['title', 'company_name', 'employment_type', 'owner']

admin.site.register(JobAdvert, JobAdvertDisplay)
