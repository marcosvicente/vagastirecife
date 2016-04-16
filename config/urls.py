""" job_board_project URL Configuration """

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('job_board.urls'))
]
