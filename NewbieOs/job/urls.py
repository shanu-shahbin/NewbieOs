from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('job/<int:id>/', views.job_details, name='job_details'),
    path('saved-jobs/', views.saved_jobs, name='saved_jobs'),
    path('applied-jobs/', views.applied_jobs, name='applied_jobs'),
    path('save-or-remove-job/', views.save_or_remove_job, name='save_job'),
    path('apply-job/<int:job_id>/', views.apply_job, name='apply_job'),
    path('remove-saved-job/', views.remove_saved_job, name='remove_saved_job'),
]
