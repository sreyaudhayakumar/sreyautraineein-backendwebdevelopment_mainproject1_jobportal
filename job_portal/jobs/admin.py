from django.contrib import admin
from jobs.models import CustomUser, JobSeekerProfile,JobListing, JobApplication



admin.site.register(CustomUser)
admin.site.register(JobSeekerProfile)
admin.site.register(JobListing)
admin.site.register(JobApplication)
