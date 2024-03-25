from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm, JobSeekerProfileForm, ProfileUpdateForm, CompanyProfileForm, JobListingForm, JobApplicationForm
from .models import CustomUser, JobSeekerProfile, CompanyProfile, JobListing, JobApplication
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import logout


def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def admin_base(request):
    company_profile = CompanyProfile.objects.first() 
    return render(request, 'admin_base.html', {'company_profile': company_profile})


def base2(request):
    company_profile = CompanyProfile.objects.first() 
    application = JobApplication.objects.first() 

    context = {
        'company_profile': company_profile,
        'application': application,
    }

    return render(request, 'base2.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_type = form.cleaned_data['user_type']
            user.user_type = user_type
            user.date_joined = datetime.now()
            user.last_login = timezone.now()
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_type == 'job_seeker':
                    return redirect('base')
                elif user.user_type == 'employer':
                    return redirect('base2')
                else:
                    return redirect('admin_base')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home') 

@login_required
def create_profile(request):
    try:
        profile = JobSeekerProfile.objects.get(user=request.user)
        return redirect('update_profile')
    except JobSeekerProfile.DoesNotExist:
        if request.method == 'POST':
            profile_form = JobSeekerProfileForm(request.POST, request.FILES)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = request.user
                profile.save()
                return redirect('base')
        else:
            profile_form = JobSeekerProfileForm()
        return render(request, 'create_profile.html', {'form': profile_form})

@login_required
def update_profile(request):
    profile = request.user.jobseekerprofile
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile_detail')
    else:
        profile_form = ProfileUpdateForm(instance=profile)
    return render(request, 'update_profile.html', {'form': profile_form})

def profile_detail(request):
    try:
        profile = JobSeekerProfile.objects.get(user=request.user)
    except JobSeekerProfile.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'profile_details.html', {'profile': profile})

def job_list(request):
    job_listings = JobListing.objects.all()
    return render(request, 'job_list.html', {'job_listings': job_listings})

def job_detail(request, job_id):
    job_listing = JobListing.objects.get(id=job_id)
    form = JobApplicationForm()
    return render(request, 'job_detail.html', {'job_listing': job_listing, 'form': form})

def apply_job(request, job_id):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job_listing = JobListing.objects.get(id=job_id)
            application = form.save(commit=False)
            application.job_listing = job_listing
            application.applicant = request.user
            application.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm()
    return render(request, 'apply_job.html', {'form': form})

@login_required
def create_job_listing(request):
    if request.method == 'POST':
        form = JobListingForm(request.POST)
        if form.is_valid():
            job_listing = form.save(commit=False)
            job_listing.save()
            return redirect('job_list')
    else:
        form = JobListingForm()
    return render(request, 'create_job_listing.html', {'form': form})

def create_company_profile(request):
    if request.method == 'POST':
        form = CompanyProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base2')
    else:
        form = CompanyProfileForm()
    return render(request, 'create_company_profile.html', {'form': form})

@login_required
def update_company_profile(request, pk):
    company_profile = CompanyProfile.objects.get(pk=pk)
    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, instance=company_profile)
        if form.is_valid():
            form.save()
            return redirect('base2')
    else:
        form = CompanyProfileForm(instance=company_profile)
    return render(request, 'update_company_profile.html', {'form': form})

def edit_job_listing(request, job_id):
    job_listing = get_object_or_404(JobListing, id=job_id)
    if request.method == 'POST':
        form = JobListingForm(request.POST, instance=job_listing)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobListingForm(instance=job_listing)
    return render(request, 'edit_job_listing.html', {'form': form})

def delete_job_listing(request, job_id):
    job_listing = get_object_or_404(JobListing, id=job_id)
    job_listing.delete()
    return redirect('job_list')

def job_detail(request, job_id):
    job = JobListing.objects.get(id=job_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job_listing = job
            application.applicant = request.user
            application.save()
            return redirect('application_status')
    else:
        form = JobApplicationForm()
    return render(request, 'job_detail.html', {'job': job, 'form': form})

def application_status(request):
    applications = JobApplication.objects.filter(applicant=request.user)
    return render(request, 'application_status.html', {'applications': applications})

def view_job_applications(request):
    applications = JobApplication.objects.all()
    return render(request, 'view_job_applications.html', {'applications': applications})

def manage_job_applications(request):
    applications = JobApplication.objects.all()
    return render(request, 'manage_job_applications.html', {'applications': applications})

def delete_job_application(request, application_id):
    application = get_object_or_404(JobApplication, pk=application_id)
    if request.method == 'POST':
        application.delete()
        return redirect('manage_job_applications')
    return render(request, 'confirm_delete_applications.html', {'application': application})


def accept_job_application(request, application_id):
    application = get_object_or_404(JobApplication, pk=application_id)
    if request.method == 'POST':
        application.status = 'accepted'
        application.save()
        return redirect('manage_job_applications')
    return render(request, 'confirm_accept_application.html', {'application': application})

def confirm_accept_application(request, application_id):
    application = get_object_or_404(JobApplication, pk=application_id)
    return render(request, 'confirm_accept_application.html', {'application': application})

from .forms import JobSearchForm

def search_jobs(request):
    form = JobSearchForm(request.GET)
    query = request.GET.get('query')
    location = request.GET.get('location')
    company = request.GET.get('company')  
    sort_by = request.GET.get('sort_by')

    jobs = JobListing.objects.all()


    if query:
        jobs = jobs.filter(title__icontains=query)
    if location:
        jobs = jobs.filter(location__icontains=location)
    if company:
        jobs = jobs.filter(company__icontains=company)
    
    if sort_by == 'title':
        jobs = jobs.order_by('title')
    elif sort_by == 'location':
        jobs = jobs.order_by('location')
    elif sort_by == 'company':
        jobs = jobs.order_by('company')
    

    context = {
        'form': form,
        'jobs': jobs,
        'query': query,
        'location': location,
        'company': company,
        'sort_by': sort_by,
    }

    return render(request, 'job_search_results.html', context)

