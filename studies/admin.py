from django.contrib import admin
from . import models
admin.site.site_header = "Al - Najah"
admin.site.index_title = "Welcome Admin"
admin.site.site_title = "Admin"

class subjectItem(admin.TabularInline):
    model=models.Section.subject.through
# Register your models here.
@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.email)
class MajorAdmin(admin.ModelAdmin):
    list_display = ['email','canAccess']


@admin.register(models.setting)
class settingsAdmin(admin.ModelAdmin):
    list_display = ['WelcomePageText']

@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name','number']

@admin.register(models.Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['name','isPublic']
    inlines =[subjectItem]
    exclude = ['subject']



