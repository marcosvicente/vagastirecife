from django.contrib import admin

from job_board.models import Job, Category, JobType

class JobAdmin(admin.ModelAdmin):
    ordering = ['-timestamp']

admin.site.register(Job, JobAdmin)
admin.site.register(Category)
admin.site.register(JobType)