from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})