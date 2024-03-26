from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('base2/', views.base2, name='base2'),
    path('admin_base/', views.admin_base, name='admin_base'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_profile/',views.create_profile,name='create_profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('profile_detail/', views.profile_detail, name='profile_detail'),
    path('jobs/', views.job_list, name='job_list'),
    path('job/<int:job_id>/apply/', views.apply_job, name='apply_job'),
    path('applications/', views.application_status, name='application_status'),
    path('create-job/', views.create_job_listing, name='create_job_listing'),
    path('create-company-profile/', views.create_company_profile, name='create_company_profile'),
    path('update-company-profile/<int:pk>/', views.update_company_profile, name='update_company_profile'),
    path('edit-job/<int:job_id>/', views.edit_job_listing, name='edit_job_listing'),
    path('delete-job/<int:job_id>/', views.delete_job_listing, name='delete_job_listing'),
    path('application/status/', views.application_status, name='application_status'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('view/job/applications/', views.view_job_applications, name='view_job_applications'),
    path('manage/job/applications/', views.manage_job_applications, name='manage_job_applications'),
    path('delete/job/application/<int:application_id>/', views.delete_job_application, name='delete_job_application'),
    path('confirm/accept/application/<int:application_id>/', views.confirm_accept_application, name='confirm_accept_application'),
    path('accept/job/application/<int:application_id>/', views.accept_job_application, name='accept_job_application'),
    path('search_jobs/', views.search_jobs, name='search_jobs'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    # path('job_application_success/', views.job_application_success, name='job_application_success'),
    # path('send_job_application_email/',views.send_job_application_email, name='send_job_application_email'),
    # path('review_status/', views.review_status, name='review_status'),
    # path('submit_review/', views.submit_review, name='submit_review'),
    # path('view_latest_review/', views.view_latest_review, name='view_latest_review'),
    
]

