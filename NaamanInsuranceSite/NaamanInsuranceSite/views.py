from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

class IndexView(generic.TemplateView):
    template_name = 'insurance/index.html'

class ContactView(generic.TemplateView):
    template_name = 'insurance/contact.html'
    



