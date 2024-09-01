from django.contrib import admin
from django.utils.html import format_html
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('name', 'email', 'user_type', 'number', 'profile_pic_tag', 'created_at')
    # Fields to filter in the sidebar
    list_filter = ('user_type', 'created_at')
    # Fields to search by in the admin list view
    search_fields = ('name', 'email', 'number')
    # Order of the list view
    ordering = ('-created_at',)
    # Fields to be read-only
    readonly_fields = ('created_at', 'updated_at', 'profile_pic_tag')
    # Field grouping for a more organized view in the detail page
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'name', 'email', 'user_type', 'number')
        }),
        ('Profile Picture', {
            'fields': ('profile_pic', 'profile_pic_tag')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    # Method to display the profile picture as a small thumbnail in the list view
    def profile_pic_tag(self, obj):
        if obj.profile_pic:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />'.format(obj.profile_pic.url))
        return '-'

    profile_pic_tag.short_description = 'Profile Picture'

    # Optionally, add actions for batch operations
    actions = ['mark_as_admin', 'mark_as_job_seeker', 'mark_as_recruiter']

    def mark_as_admin(self, request, queryset):
        queryset.update(user_type='admin')
    mark_as_admin.short_description = "Mark selected users as Admin"

    def mark_as_job_seeker(self, request, queryset):
        queryset.update(user_type='job_seeker')
    mark_as_job_seeker.short_description = "Mark selected users as Job Seeker"

    def mark_as_recruiter(self, request, queryset):
        queryset.update(user_type='recruiter')
    mark_as_recruiter.short_description = "Mark selected users as Recruiter"
