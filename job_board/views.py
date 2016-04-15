from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse

from .forms import CreateJobForm
from .models import Job

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    return render(request, 'jobs/job_detail.html', {'job': job})

def job_create(request):
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            job = form.save()
            messages.success(request, "Vaga anunciada com sucesso.")
            return redirect('job.views.job_detail', slug=job.slug)
    else:
        form = CreateJobForm()
    return render(request, 'jobs/job_create.html', {'form': form})