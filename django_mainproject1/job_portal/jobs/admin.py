from django.contrib import admin
from .models import CustomUser, JobSeekerProfile, EmployerProfile, JobListing, Application, ReportedIssue, AdminModel

# Register your models here

admin.site.register(CustomUser)
admin.site.register(JobSeekerProfile)
admin.site.register(EmployerProfile)
admin.site.register(JobListing)
admin.site.register(Application)
admin.site.register(ReportedIssue)
admin.site.register(AdminModel)
