from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Angebot

# Create your views here.

def index(request):
    angebot_list = Angebot.objects.order_by('-pub_date')[:5]
    template = loader.get_template('unternehmen/index.html')
    context = {
        'angebot_list': angebot_list,
        }

    return HttpResponse(template.render(context, request))
