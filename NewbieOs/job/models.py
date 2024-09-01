from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from company.models import Company

class Ad(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ads/')
    link = models.URLField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('Internship', 'Internship'),
        ('Job', 'Job'),
    ]
    WORK_MODE_CHOICES = [
        ('On-site', 'On-site'),
        ('Remote', 'Remote'),
    ]

    job_title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs')
    job_posted_date = models.DateField()
    job_applylast_date = models.DateField(null=True, blank=True)
    experience_level = models.CharField(max_length=100)
    work_mode = models.CharField(max_length=10, choices=WORK_MODE_CHOICES)
    responsibilities = RichTextField(null=True, blank=True)
    qualifications = RichTextField(null=True, blank=True)
    skill1 = models.CharField(max_length=100, null=True, blank=True)
    skill2 = models.CharField(max_length=100, null=True, blank=True)
    skill3 = models.CharField(max_length=100, null=True, blank=True)
    skill4 = models.CharField(max_length=100, null=True, blank=True)
    pay_range = models.CharField(max_length=100)
    job_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.job_title

class SavedJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_jobs')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='saved_by_users')
    saved_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} saved {self.job.job_title}"

class AppliedJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applied_jobs')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applied_by_users')
    applied_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"{self.user.username} applied for {self.job.job_title} on {self.applied_date}"
