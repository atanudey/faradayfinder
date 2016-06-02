"""
Defines view for chat
"""
import json
from django.core import serializers
from django.db.models import Q
import logging
from jobs.models import Job as Jobo
from contents.models import Lab as Labo
from contents.models import ChatMessages as Chato
from django.http import HttpResponse
from django.views.generic import View
from django.template import loader, RequestContext
from django.contrib import messages
from datetime import datetime

LOGGER = logging.getLogger(__name__)

class ChatLogin(View):
    template_name = 'o/dialog-login.html'

    def get(self, request, *args, **kwargs):
        context = {}

        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))
    
class ChatToolbar(View):
    template_name = 'o/toolbar.html'

    def get(self, request, *args, **kwargs):
        context = {}

        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))
    
class ChatMain(View):
    template_name = 'o/main-chat.html'

    def get(self, request, *args, **kwargs):
        context = {}

        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))
    
class ChatOptions(View):
    template_name = 'o/options.html'

    def get(self, request, *args, **kwargs):
        context = {}

        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))

class ChatSaveMessages(View):    
    def get(self, request, *args, **kwargs):
        sndr = request.GET.get('sndr')
        recv = request.GET.get('recv')
        sort_by = "id"                 
        if sndr != "" and recv != "":
            result = []
            rs = Chato.objects.filter(Q(sender_id=sndr,receiver_id=recv) | Q(sender_id=recv,receiver_id=sndr)).order_by(sort_by)
            for r in rs:
                data = serializers.serialize('json', [r,])
                struct = json.loads(data)                
                result.append(struct[0]["fields"])
                   
        return HttpResponse(json.dumps(result), content_type="application/json")
    
    def post(self, request, *args, **kwargs):
        msg = eval(request.POST.get('msg'))
        request.session['in_conversation'] = True        
        chato = Chato(**msg);
        chatentry  = chato.save();
        result = {'success': True, 'in_conversation': request.session.get('in_conversation', False)}
        return HttpResponse(json.dumps(result), content_type="application/json")