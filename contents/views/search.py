"""
Defines view for project
"""

import logging
from jobs.models import Job as Jobo
from contents.models import Lab as Labo
from django.http import HttpResponse
# from django.views.generic import View, UpdateView, DetailView
from django.views.generic import View
# from contents.forms import projects
from django.template import loader, RequestContext
from django.contrib import messages
from datetime import datetime

LOGGER = logging.getLogger(__name__)


class SearchLabs(View):

    template_name = 'o/search.html'

    def get(self, request, *args, **kwargs):
        context = {}

        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))


class SearchProjects(View):

    template_name = 'o/search.html'

    def get(self, request, *args, **kwargs):
        context = {}

        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))


class SearchEvents(View):

    template_name = 'o/search.html'

    def get(self, request, *args, **kwargs):
        context = {}

        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))


class SearchEquipments(View):

    template_name = 'o/search.html'

    def get(self, request, *args, **kwargs):
        context = {}

        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))


class SearchJobs(View):

    template_name = 'o/search-job.html'

    def get(self, request, *args, **kwargs):
        context = {}

        # taking flush messages
        load_message = messages.get_messages(request)
        for storage in load_message:
            context['flush_message'] = storage

        sort_by = "job_title"
        if request.GET.get('sort_by'):
            sort_by = request.GET.get('sort_by')

        # if request.user.is_authenticated():
        #     jobs = Jobo.objects.filter(user=request.user, is_paid=True,
        #                                close_date__gt=datetime.now()
        #                                ).order_by(sort_by)
        # else:
        jobs = Jobo.objects.filter(is_paid=True,
                                   close_date__gt=datetime.now()
                                   ).order_by(sort_by)

        if request.GET.get('sort_type') == "desc":
            jobs = jobs.reverse()

        if self.kwargs.get("job_starts_with"):
            jobs = jobs.filter(job_title__istartswith=self.kwargs.get("job_starts_with"))

        if request.GET.get('search'):
            filter = sort_by + '__contains'
            jobs = jobs.filter(**{filter: request.GET.get('search')})

        context['jobs'] = jobs
        
        context['jobs_joined'] = []

        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))
