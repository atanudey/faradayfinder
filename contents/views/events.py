"""
Defines view for events
"""

import json
import logging
from contents.models import Event as Evento
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, UpdateView, DetailView
from contents.forms import events
from django.template import loader, RequestContext
from django.contrib import messages
from django.shortcuts import get_object_or_404

LOGGER = logging.getLogger(__name__)

class UpdateEvent(UpdateView):
    template_name = 'o/update-event.html'
    form_class = events.FormUpdateEvent
    model = Evento
    success_url = '/my-events/'

    def get(self, request, **kwargs):
        self.object = Evento.objects.get(
            id=self.kwargs.get("event_id"),
            user=request.user,
            is_deleted=False
        )
        form = self.get_form(self.form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self):
        return Evento.objects.get(
            pk=self.kwargs.get("event_id")
        )


class MyEvents(View):

    template_name = 'o/my-events.html'

    def get(self, request, *args, **kwargs):
        context = {}

        # taking flush messages
        load_message = messages.get_messages(request)
        for storage in load_message:
            context['flush_message'] = storage

        # getting all the events
        events = Evento.objects.filter(user=request.user, is_deleted=False)
        context['events'] = events

        context['events_joined'] = []

        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))


class Event(View):
    template_name = 'o/create-event.html'
    form = events.FormEvents

    def display(self, request, *args, **kwargs):
        context = {
            'form': self.form if not 'form' in kwargs else kwargs['form'],
            'errors': kwargs.get('errors')
        }

        # password protected detail
        is_private = request.POST.get('is_private', False)
        if is_private in [True, 'True']:
            context['display_password_protected'] = True

        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))

    def get(self, request, *args, **kwargs):
        return self.display(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your event "{}" has been created '
                                      'successfully' .
                             format(request.POST['name']))
            return HttpResponseRedirect('/my-events/')
        else:
            kwargs['errors'] = form.errors
        kwargs['form'] = form
        return self.display(request, *args, **kwargs)


class ViewEvent(DetailView):

    model = Evento
    template_name = 'object_pic_box.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        return Evento.objects.filter(id=pk, is_deleted=False)

    def get_context_data(self, **kwargs):
        context = super(ViewEvent, self).get_context_data(**kwargs)
        context['object'] = self.get_queryset()[0]
        return context
