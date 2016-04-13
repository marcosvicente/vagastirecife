from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    category = models.ForeignKey('Category')
    job_type = models.ForeignKey('JobType')
    url = models.URLField()
    company = models.CharField(max_length=140)
    salary = models.DecimalField(default=0, max_digits=19, decimal_places=2)
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