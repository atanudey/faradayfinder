"""
Defines view for labs
"""

import json
import logging
from contents.models import Institute, Lab as Labo, Department, LabMember
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, UpdateView, DetailView, FormView
from contents.forms.labs import FormLabs, FormUpdateLabs
from django.template import loader, RequestContext
from django.contrib import messages


LOGGER = logging.getLogger(__name__)


class UpdateLab(UpdateView):
    template_name = 'o/update-lab.html'
    form_class = FormUpdateLabs
    model = Labo
    success_url = '/my-labs/'

    def get(self, request, **kwargs):
        self.object = Labo.objects.get(
            id=self.kwargs.get("lab_id"),
            user=request.user,
            is_deleted=False
        )
        form = self.get_form(self.form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self):
        return Labo.objects.get(
            pk=self.kwargs.get("lab_id")
        )


class MyLabs(View):

    template_name = 'o/my-labs.html'

    def get(self, request, *args, **kwargs):
        context = {}

        # taking flush messages
        load_message = messages.get_messages(request)
        for storage in load_message:
            context['flush_message'] = storage

        # getting all the labs
        labs = Labo.objects.filter(user=request.user, is_deleted=False)
        context['labs'] = labs

        context['labs_joined'] = []

        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))


class Lab(View):

    template_name = 'o/create-lab.html'
    form = FormLabs

    def display(self, request, *args, **kwargs):

        context = {
            'form': self.form if not 'form' in kwargs else kwargs['form'],
            'errors': kwargs.get('errors')
        }

        # Department selection on selection on institute
        institute = request.POST.get('institute')
        try:
            department = int(request.POST.get('department'))
        except:
            department = 0

        if institute:
            departments = Department.objects.filter(
                is_deleted=False,
                institute=institute
            )
            context['departments'] = departments
        context['department'] = department

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
            messages.success(request, 'Your lab "{}" has been created '
                                      'successfully' .
                             format(request.POST['name']))
            return HttpResponseRedirect('/my-labs/')
        else:
            kwargs['errors'] = form.errors
        kwargs['form'] = form
        return self.display(request, *args, **kwargs)


class GetDepartments(View):

    def get(self, request, institute_id, *args, **kwargs):
        departments = list(
            Department.objects.values('id', 'name').filter(
                is_deleted=False,
                institute_id=institute_id).order_by('name')
        )

        return HttpResponse(
            json.dumps(departments), mimetype='application/json'
        )


class ViewLab(FormView, DetailView):

    model = Labo
    template_name = 'o/object.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        lab = Labo.objects.filter(id=pk, is_deleted=False)
        return lab

    def check_object_access(self, object):

        # check access for object
        # TODO check if user has group access then allow him to access object
        access = False
        if not object.password:
            access = True
        elif self.request.user.id == object.user.id:
            access = True
        if 'lab_{}' . format(object.id) in self.request.session:
            access = True
        return access

    def get_object_access(self, lab):

        join_access = None
        if self.request.user.is_authenticated():
            if self.request.user.id == lab.user.id:
                pass
            else:
                try:
                    LabMember.objects.get(lab_id=lab.id, user_id=self.request.user.id)
                    join_access = 'Leave Lab'
                except:
                    join_access = 'Join Lab'
        else:
            join_access = 'Visitor'
        return join_access

    def get_context_data(self, **kwargs):

        object = self.get_queryset()[0]

        # check object access
        access = self.check_object_access(object)
        if access is False:
            self.template_name = 'o/password-protected.html'

        context = super(ViewLab, self).get_context_data(**kwargs)
        context['object'] = object
        context['ObjectType'] = 'lab'
        context['ObjectJoinAccess'] = self.get_object_access(object)
        return context

    def post(self, request, *args, **kwargs):

        context = {'access': False}
        pk = kwargs.get('pk')
        request_type = request.POST.get('type', '')

        try:
            lab = Labo.objects.get(id=pk, is_deleted=False)

            if request_type == 'join':
                try:
                    LabMember.objects.get(lab_id=pk, user_id=request.user.id).delete()
                    context['type'] = 'Join Lab'
                except:
                    LabMember.objects.create(lab_id=pk, user_id=request.user.id)
                    context['type'] = 'Leave Lab'
                context['access'] = True
            else:
                if request.POST.get('password') == lab.password:
                    context['access'] = True
                    request.session['lab_{}' . format(pk)] = True
        except Exception as e:
            context['e'] = str(e)
        return HttpResponse(content=json.dumps(context), status=200)
