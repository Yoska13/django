from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

class BidsView(generic.TemplateView):
    template_name = 'Bids/bids.html'



