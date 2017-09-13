import logging

from django.shortcuts import render, redirect

from offer.forms import OfferForm
from offer.models import Offer


# Create your views here.


def index(request):
    application_list = Offer.objects.order_by('-application_date')
    context = {
        'application_list': application_list,
    }
    return render(request=request, template_name='offer/index.html', context=context)


def add_offer(request):
    form = OfferForm()

    if request.method == 'POST':
        form = OfferForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(to='/')
        else:
            logging.error(form.errors)

    return render(request=request, template_name='offer/add_offer.html', context={'form': form})
