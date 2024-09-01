from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('job_seeker', 'Job Seeker'),
        ('recruiter', 'Recruiter'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Each Customer has one User profile
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)  # Ensure email is unique in Customer
    profile_pic = models.ImageField(upload_to='profilepics/', default='profilepics/default.jpg', null=True, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    number = models.CharField(max_length=20, unique=True, null=True, blank=True)  # Ensure phone number is unique
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name if self.name else "Unnamed Customer"

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['-created_at']
