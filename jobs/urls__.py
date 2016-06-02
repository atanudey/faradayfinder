from django.conf.urls import patterns, url

from jobs import views as views_jobs

urlpatterns = patterns('',
                       url(r'^$', views_jobs.ViewJob.as_view(), name='index'),
                       )
