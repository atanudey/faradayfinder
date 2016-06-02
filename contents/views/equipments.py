"""
Defines view for project
"""

import json
import logging
from contents.models import Equipment as Equipmento
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, UpdateView, DetailView
from contents.forms import equipments
from django.template import loader, RequestContext
from django.contrib import messages
from django.shortcuts import get_object_or_404


LOGGER = logging.getLogger(__name__)


class UpdateEquipment(UpdateView):
    template_name = 'o/update-equipment.html'
    form_class = equipments.FormUpdateEquipment
    model = Equipmento
    success_url = '/my-equipments/'

    def get(self, request, **kwargs):
        self.object = Equipmento.objects.get(
            id=self.kwargs.get("equipment_id"),
            user=request.user,
            is_deleted=False
        )
        form = self.get_form(self.form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self):
        return Equipmento.objects.get(
            pk=self.kwargs.get("equipment_id")
        )


class MyEquipments(View):

    template_name = 'o/my-equipments.html'

    def get(self, request, *args, **kwargs):
        context = {}

        # taking flush messages
        load_message = messages.get_messages(request)
        for storage in load_message:
            context['flush_message'] = storage

        # getting all the equipments
        equipments = Equipmento.objects.filter(user=request.user,
                                               is_deleted=False)
        context['equipments'] = equipments

        context['equipments_joined'] = []

        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))


class Equipment(View):

    template_name = 'o/create-equipment.html'
    form = equipments.FormEquipments

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
            messages.success(request, 'Your equipment "{}" has been created '
                                      'successfully' .
                             format(request.POST['name']))
            return HttpResponseRedirect('/my-equipments/')
        else:
            kwargs['errors'] = form.errors
        kwargs['form'] = form
        return self.display(request, *args, **kwargs)


class ViewEquipment(DetailView):

    model = Equipmento
    template_name = 'object_pic_box.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        return Equipmento.objects.filter(id=pk, is_deleted=False)

    def get_context_data(self, **kwargs):
        context = super(ViewEquipment, self).get_context_data(**kwargs)
        context['object'] = self.get_queryset()[0]
        return context
