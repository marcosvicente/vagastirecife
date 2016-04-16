from django.contrib import admin

from job_board.models import Job, Category, JobType


class JobAdmin(admin.ModelAdmin):
    ordering = ['-timestamp']


class CategoryAdmin(admin.ModelAdmin):
    list_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Job, JobAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(JobType)