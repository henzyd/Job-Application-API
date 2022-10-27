from django.contrib import admin
from .models import JobAdvert, JobApplication

# Register your models here.

class JobAdvertDisplay(admin.ModelAdmin):
    list_display = ['title', 'company_name', 'employment_type', 'owner']

admin.site.register(JobAdvert, JobAdvertDisplay)



class JobApplicationDisplay(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email_address', 'applicants']

admin.site.register(JobApplication, JobApplicationDisplay)
