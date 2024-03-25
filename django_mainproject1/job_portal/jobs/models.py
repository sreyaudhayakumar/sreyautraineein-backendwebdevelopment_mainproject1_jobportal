

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('employer', 'Employer/Recruiter'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)



    groups = models.ManyToManyField(
        Group,
        related_name='custom_users',
        related_query_name='custom_user'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_users',
        related_query_name='custom_user'
    )

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

try:
    Group._meta.get_field('custom_users').related_name = 'custom_groups'
except Exception as e:
    print("Error occurred while setting related name for custom_groups:", e)

try:
    Permission._meta.get_field('custom_users').related_name = 'custom_user_permissions'
except Exception as e:
    print("Error occurred while setting related name for custom_user_permissions:", e)
    


class JobSeekerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')

class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)

class JobListing(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    required_qualifications = models.TextField()
    desired_qualifications = models.TextField()
    responsibilities = models.TextField()
    application_deadline = models.DateTimeField()
    salary_range = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=100)
    company_benefits = models.TextField()
    how_to_apply = models.TextField()
  

class Application(models.Model):
    job_seeker = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE)
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    cover_letter = models.TextField()

class ReportedIssue(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    issue_description = models.TextField()
 

class AdminModel(models.Model):
  
    pass
