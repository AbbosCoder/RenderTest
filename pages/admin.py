from django.contrib import admin
from .models import Profile, Project, Skill, MyInfo, ContactMessage, Experience

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role')
    search_fields = ('full_name', 'role')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies')
    search_fields = ('title', 'technologies', 'description')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    list_filter = ('level',)
    search_fields = ('name',)

@admin.register(MyInfo)
class MyInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'created_at')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'start_date', 'end_date')
    list_filter = ('company',)
    search_fields = ('job_title', 'company', 'description')