from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.job_list, name='index'),
    url(r'vagas/adicionar-vaga/$', views.job_create, name='job_create'),
    url(r'vagas/(?P<slug>[\w-]+)/$', views.job_detail, name='job_detail')
]