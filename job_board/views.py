from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Job

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    return render(request, 'jobs/job_detail.html', {'job': job})