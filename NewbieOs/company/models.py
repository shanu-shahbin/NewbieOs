from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=255)
    employees = models.CharField(max_length=50,null=True,blank=True)  # You could also use IntegerField if you prefer exact numbers
    industry = models.CharField(max_length=100,null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    image = models.ImageField(upload_to='company_images/', null=True, blank=True)  # Optional image field
    logo = models.ImageField(upload_to='company_logo/', null=True, blank=True)  # Optional image field
    email=models.EmailField(null=True,blank=True)
    company_website = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name