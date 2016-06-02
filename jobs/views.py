"""
Defines view for project
"""

import logging
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, UpdateView, DetailView
from django.template import loader, RequestContext
from django.contrib import messages
from jobs.forms import FormUpdateJob, FormJobs
from jobs.models import Job as Jobo
from jobs.models import PaymentInfo as PI
from django.conf import settings
from datetime import datetime

LOGGER = logging.getLogger(__name__)

class UpdateJob(UpdateView):
    template_name = 'o/update-job.html'
    form_class = FormUpdateJob
    model = Jobo
    success_url = '/search/jobs/'

    def get(self, request, **kwargs):
        self.object = Jobo.objects.get(
            id=self.kwargs.get("job_id")
        )
        
        LOGGER.info("UPDATE JOB WITH id {} ".format(self.kwargs.get("job_id")));
        LOGGER.info("UPDATE JOB WITH user {} ".format(request.user));
        
        form = self.get_form(self.form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        job_model = Jobo.objects.get(pk=self.kwargs.get("job_id"))
        return job_model


class MyJobs(View):

    template_name = 'o/my-jobs.html'

    def get(self, request, *args, **kwargs):
        context = {}

        # taking flush messages
        load_message = messages.get_messages(request)
        for storage in load_message:
            context['flush_message'] = storage

        # getting all the jobs        
        jobs = Jobo.objects.filter(user=request.user, close_date__gt=datetime.now(), is_paid=True)
        context['jobs'] = jobs

        context['jobs_joined'] = []

        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))


class JobPayment(View):

    template_name = 'o/job-payment.html'
    form = FormJobs

    def display(self, request, *args, **kwargs):
        context = {
            'form': self.form if 'form' not in kwargs else kwargs['form'],
            'errors': kwargs.get('errors'),
            'payment_url': settings.PAYMENT_GATEWAY_URL,
            'payment_email': settings.PAYMENT_MERCHANT_EMAIL,
        }

        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))

    def get(self, request, *args, **kwargs):
        context = {}
        form = self.form(request.session.get('job_post_data'))
        if form.is_valid():
            job_model = form.save(commit=False)
            job_model.user = request.user
            new_job = form.save()
            
            post_data = request.session.get('job_post_data')
                        
            context['new_job_id'] = new_job.id
            context['payment_url'] = settings.PAYMENT_GATEWAY_URL
            context['payment_email'] = settings.PAYMENT_MERCHANT_EMAIL            
            context['payment_bn'] = settings.PAYMENT_BUTTON
            context['payment_item_name'] = settings.PAYMENT_ITEM_NAME
            context['payment_item_number'] = settings.PAYMENT_ITEM_NUMBER
            context['payment_amount'] = settings.PAYMENT_AMOUNT
            context['payment_tax'] = settings.PAYMENT_TAX
            context['payment_quantity'] = settings.PAYMENT_QUANTITY
            context['payment_no_note'] = settings.PAYMENT_NO_NOTE
            context['payment_currency_code'] = settings.PAYMENT_CURRENCY_CODE
            context['payment_address_override'] = settings.PAYMENT_ADDRESS_OVERRIDE
            context['payment_first_name'] = settings.PAYMENT_FIRST_NAME
            context['payment_last_name'] = settings.PAYMENT_LAST_NAME
            context['payment_address1'] = settings.PAYMENT_ADDRESS1
            context['payment_city'] = settings.PAYMENT_CITY
            context['payment_state'] = settings.PAYMENT_STATE
            context['payment_zip'] = settings.PAYMENT_ZIP
            context['payment_country'] = settings.PAYMENT_COUNTRY
            
            request.session['new_job_id'] = new_job.id
        else:
            kwargs['errors'] = form.errors

        kwargs['form'] = form
        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)

        return HttpResponse(template.render(data))

    def post(self, request, *args, **kwargs):
        return self.display(request, *args, **kwargs)


class Job(View):

    template_name = 'o/post-job.html'
    model = Jobo
    form = FormJobs

    def display(self, request, *args, **kwargs):
        context = {
            'form': self.form if 'form' not in kwargs else kwargs['form'],
            'errors': kwargs.get('errors')
        }

        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))

    def get(self, request, *args, **kwargs):        
        if request.GET.get('cm'):            
            exists = PI.objects.filter(pk=request.GET.get('cm')).exists()
            if exists is False:
                payment = PI()
                
                payment.cm = request.GET.get('cm');
                payment.tx = request.GET.get('tx');
                payment.cc = request.GET.get('cc');
                payment.amt = request.GET.get('amt');
                payment.item_number = request.GET.get('item_number');
                payment.st = request.GET.get('st');
                
                payment.save();
                
                job_model = Jobo.objects.get(pk=request.GET.get('cm'))
                if (request.GET.get('st') == 'Completed' and float(request.GET.get('amt')) == float(settings.PAYMENT_AMOUNT)):
                    job_model.is_paid = True
                    job_model.save()
    
                    messages.success(request, 'Your job "{}" has been created '
                                              'successfully'
                                              . format(job_model.job_title))
                    return HttpResponseRedirect('/search/jobs/')
                else:
                    job_model.delete()
                    messages.success(request, 'Some error occurred with your '
                                              'payment! Failed to create the job!')
                    return HttpResponseRedirect('/search/jobs/')

        elif request.session.get('new_job_id'):            
            job_model = Jobo.objects.get(pk=request.session.get('new_job_id'))
            job_model.delete()
            
            del request.session['new_job_id']
            messages.success(request, 'Payment canceled by the user! '
                                      'Failed to create the job!')
            return HttpResponseRedirect('/search/jobs/')
            
        return self.display(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            request.session['job_post_data'] = request.POST
            return HttpResponseRedirect('/jobs/job-payment/')
        else:
            kwargs['errors'] = form.errors

        kwargs['form'] = form
        return self.display(request, *args, **kwargs)


class ViewJob(DetailView):

    model = Jobo
    template_name = 'o/job-details.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        return Jobo.objects.filter(id=pk).select_related('lab')

    def get_context_data(self, **kwargs):
        context = super(ViewJob, self).get_context_data(**kwargs)
        obj = self.get_queryset()[0]
        context['object'] = obj
        #import pdb; pdb.set_trace()
        context['currency'] = settings.CURRENCY_LIST[obj.pay_rate_currency_code]
        return context
