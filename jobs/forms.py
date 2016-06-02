from django import forms
from jobs import models


class FormUpdateJob(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        instance = kwargs['instance']
        self.user_id = instance.user.id
        super(FormUpdateJob, self).__init__(*args, **kwargs)
        fields_name = ['lab', 'open_date', 'job_title', 'type', 'temporary',
                       'hours_per_week', 'work_schedule_summary',
                       'work_study_job', 'department', 'pay_rate_range_max',
                       'pay_rate_range_min', 'close_date', 'job_summary',
                       'responsibilities', 'minimum_qualification',
                       'preferences', 'additional_information']

    class Meta:
        model = models.Job
        exclude_fields = ['is_paid', 'date_joined', 'date_updated']


class FormJobs(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(FormJobs, self).__init__(*args, **kwargs)
        fields_name = ['lab', 'open_date', 'job_title', 'type', 'temporary',
                       'hours_per_week', 'work_schedule_summary',
                       'work_study_job', 'department', 'pay_rate_range_max',
                       'pay_rate_range_min', 'close_date', 'job_summary',
                       'responsibilities', 'minimum_qualification',
                       'preferences', 'additional_information']

    def clean(self):
        verified_data = super(FormJobs, self).clean()
        close_date = verified_data.get("close_date")
        open_date = verified_data.get("open_date")

        if close_date and open_date:
            if open_date > close_date:
                raise forms.ValidationError(
                    "There is an ERROR as open date cannot be greater than close date"
                )
        return verified_data

    class Meta:
        model = models.Job
        exclude_fields = ['is_paid', 'date_joined', 'date_updated']
