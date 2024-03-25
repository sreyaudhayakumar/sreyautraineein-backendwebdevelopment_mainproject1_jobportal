from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('employer', 'Employer/Recruiter'),
        
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
    bio = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    
    def __str__(self):
        return self.full_name


class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class JobListing(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    qualifications = models.TextField()
    responsibilities = models.TextField()
    application_deadline = models.DateField()
    salary_range = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=50)
    benefits = models.TextField()
    how_to_apply = models.TextField()
   
    

class JobApplication(models.Model):
    job_listing = models.ForeignKey('JobListing', on_delete=models.CASCADE)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')