import logging
from django.http import HttpResponse
from django.views.generic import View
from django.template import loader, RequestContext

LOGGER = logging.getLogger(__name__)

class UserDashboard(View):
    template_name = 'o/dashboard.html'

    def get(self, request, *args, **kwargs):
        context = {}
        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))