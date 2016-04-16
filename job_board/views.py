from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse

from .forms import CreateJobForm
from .models import Job, Category


def job_create(request):
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            job = form.save()
            messages.success(request, "Vaga anunciada com sucesso.")
            return redirect('job_detail', slug=job.slug)
    else:
        form = CreateJobForm()
    return render(request, 'jobs/job_create.html', {'form': form})

def job_list(request):
    categories = Category.objects.all().order_by('name')
    jobs = Job.objects.all()
    context = {
        'jobs': jobs,
        'categories': categories
    }
    return render(request, 'jobs/job_list.html', context)

def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    return render(request, 'jobs/job_detail.html', {'job': job})