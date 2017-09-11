from django.shortcuts import render
from django.http import HttpResponse
from offer.models import Offer
# Create your views here.


def index(request):
    application_list = Offer.objects.order_by('-application_date')
    context = {
        'application_list': application_list,
    }
    return render(request=request, template_name='offer/index.html', context=context)