from django.db import models
from django.db.models.signals import pre_save

from django.utils.text import slugify

class Job(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    category = models.ForeignKey('Category')
    job_type = models.ForeignKey('JobType')
    url = models.URLField()
    company = models.CharField(max_length=140)
    salary = models.DecimalField(default=0, max_digits=19, decimal_places=2)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

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