from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, JobSeekerProfile,JobApplication




class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES)
    
    class Meta:
        model = CustomUser
        fields = ['full_name', 'username', 'email', 'password1', 'user_type']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model = JobSeekerProfile
        fields = ['full_name', 'resume', 'bio', 'experience']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = JobSeekerProfile
        fields = ['full_name', 'resume', 'bio', 'experience']
        

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['resume', 'cover_letter']





from .models import CompanyProfile

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['name', 'description', 'location']

from django import forms
from .models import JobListing

class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        exclude = ['']



from django import forms

class JobSearchForm(forms.Form):
    query = forms.CharField(label='Search Jobs', max_length=100, required=False)
    location = forms.CharField(label='Location', max_length=100, required=False)
    industry = forms.CharField(label='Industry', max_length=100, required=False)