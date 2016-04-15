from django.db import models
from django.db.models.signals import pre_save

from django.utils.text import slugify

class Job(models.Model):
    title = models.CharField(max_length=140)
    company = models.CharField(max_length=140)
    url = models.URLField()
    site = models.URLField()
    email = models.EmailField()
    category = models.ForeignKey('Category')
    job_type = models.ForeignKey('JobType')
    salary = models.DecimalField(default=0, max_digits=19, decimal_places=2)
    description = models.TextField()
    about = models.TextField()
    skills = models.TextField()
    slug = models.SlugField(unique=True, editable=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class Category(models.Model):
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class JobType(models.Model):
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


def pre_save_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    exists = Job.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" % (slug, instance.id)
    instance.slug = slug


pre_save.connect(pre_save_receiver, sender=Job)