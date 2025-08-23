from django.contrib import admin
from .models import (
    PersonalInfo, Skill, Project, Experience, 
    Education, Certification, Contact, BlogPost
)

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'location', 'updated_at']
    search_fields = ['name', 'title', 'email']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category']
    search_fields = ['name']
    ordering = ['category', 'order', 'name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'order', 'created_at']
    list_filter = ['featured', 'technologies', 'created_at']
    search_fields = ['title', 'description']
    filter_horizontal = ['technologies']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'location', 'start_date', 'end_date', 'current']
    list_filter = ['current', 'technologies_used', 'start_date']
    search_fields = ['position', 'company', 'description']
    filter_horizontal = ['technologies_used']
    date_hierarchy = 'start_date'

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'field_of_study', 'institution', 'start_date', 'end_date', 'current', 'gpa']
    list_filter = ['current', 'start_date']
    search_fields = ['degree', 'field_of_study', 'institution']
    date_hierarchy = 'start_date'

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuing_organization', 'issue_date', 'expiry_date', 'credential_id']
    list_filter = ['issue_date', 'expiry_date']
    search_fields = ['name', 'issuing_organization', 'credential_id']
    date_hierarchy = 'issue_date'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'read']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
    actions = ['mark_as_read', 'mark_as_unread']

    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_as_read.short_description = "Mark selected contacts as read"

    def mark_as_unread(self, request, queryset):
        queryset.update(read=False)
    mark_as_unread.short_description = "Mark selected contacts as unread"

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published', 'created_at', 'updated_at']
    list_filter = ['published', 'created_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
