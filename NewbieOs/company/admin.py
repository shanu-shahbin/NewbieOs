from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'industry', 'location', 'email', 'company_website', 'created_at')
    search_fields = ('company_name', 'industry', 'location', 'email')
    list_filter = ('industry', 'location', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        (None, {
            'fields': ('company_name', 'industry', 'location', 'email', 'company_website')
        }),
        ('Description & Media', {
            'fields': ('description', 'image', 'logo')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
