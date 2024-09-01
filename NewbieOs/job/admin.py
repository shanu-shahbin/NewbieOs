from django.contrib import admin
from .models import Ad, Job, Category, SavedJob, AppliedJob

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'category', 'job_posted_date', 'is_approved')
    search_fields = ('job_title', 'company__name', 'category__name')
    list_filter = ('job_type', 'work_mode', 'experience_level', 'is_approved')
    date_hierarchy = 'job_posted_date'
    ordering = ('-job_posted_date',)
    list_editable = ('is_approved',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(SavedJob)
class SavedJobAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'saved_date')
    search_fields = ('user__username', 'job__job_title')
    list_filter = ('saved_date',)

@admin.register(AppliedJob)
class AppliedJobAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'applied_date', 'status')
    search_fields = ('user__username', 'job__job_title')
    list_filter = ('status', 'applied_date')
