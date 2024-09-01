from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from .models import Category, Job, Ad, SavedJob, AppliedJob
from customers.models import Customer

def index(request):
    ad = Ad.objects.first()
    category = Category.objects.all()
    job = Job.objects.filter(is_approved=True)
    job_count = job.count()
    customer_profile = None
    if request.user.is_authenticated:
        try:
            customer_profile = Customer.objects.get(user=request.user)
        except Customer.DoesNotExist:
            customer_profile = None
    context = {
        'ad': ad,
        'category': category,
        'job': job,
        'job_count': job_count,
        'profile': customer_profile
    }
    return render(request, 'index.html', context)

def job_details(request, id):
    job = get_object_or_404(Job, id=id)
    context = {
        'job': job
    }
    return render(request, 'job_details.html', context)

@login_required
def saved_jobs(request):
    saved_jobs = SavedJob.objects.filter(user=request.user).select_related('job')
    context = {
        'saved_jobs': saved_jobs
    }
    return render(request, 'saved_jobs.html', context)

@login_required
def applied_jobs(request):
    applied_jobs = AppliedJob.objects.filter(user=request.user).select_related('job')
    context = {
        'applied_jobs': applied_jobs
    }
    return render(request, 'applied_jobs.html', context)

@login_required
def save_or_remove_job(request):
    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        job = get_object_or_404(Job, id=job_id)
        
        # Check if the job is already saved
        saved_job, created = SavedJob.objects.get_or_create(user=request.user, job=job)
        
        if not created:  # Job was already saved, so remove it
            saved_job.delete()
            return JsonResponse({'status': 'removed', 'message': 'Job removed from saved jobs.'})
        else:  # Job was not saved, so save it
            return JsonResponse({'status': 'saved', 'message': 'Job saved successfully.'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})

@login_required
def remove_saved_job(request):
    if request.method == 'POST':
        saved_job_id = request.POST.get('saved_job_id')
        try:
            saved_job = SavedJob.objects.get(id=saved_job_id, user=request.user)
            saved_job.delete()
            return JsonResponse({'status': 'success', 'message': 'Job removed successfully!'})
        except SavedJob.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Job not found.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if not AppliedJob.objects.filter(user=request.user, job=job).exists():
        AppliedJob.objects.create(user=request.user, job=job)
        messages.success(request, 'Job application submitted successfully!')
    else:
        messages.info(request, 'You have already applied for this job!')
    return redirect(reverse('job_details', args=[job_id]))
