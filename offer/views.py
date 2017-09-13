import logging

from django.shortcuts import render, redirect, HttpResponse

from offer.forms import OfferForm
from offer.models import Offer


# Create your views here.


def index(request):
    """
    首页展示
    :param request:
    :return:
    """
    application_list = Offer.objects.order_by('-application_date')
    context = {
        'application_list': application_list,
    }
    return render(request=request, template_name='offer/index.html', context=context)


def add_offer(request):
    """
    添加 offer 信息
    :param request:
    :return:
    """
    form = OfferForm()

    if request.method == 'POST':
        form = OfferForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(to='/')
        else:
            logging.error(form.errors)

    return render(request=request, template_name='offer/add_offer.html', context={'form': form})


def update_offer(request, offer_id):
    """
    编辑 offer 信息
    :param request:
    :param offer_id:
    :return:
    """
    if request.method == 'POST':
        form = OfferForm(request.POST)

        if form.is_valid():
            offer = Offer.objects.get(pk=offer_id)
            form = OfferForm(request.POST, instance=offer)
            form.save(commit=True)
            return redirect('/')
        else:
            offer = Offer.objects.get(pk=offer_id)
            form = OfferForm(instance=offer)
    else:
        offer = Offer.objects.get(pk=offer_id)
        form = OfferForm(instance=offer)

    return render(request=request, template_name='offer/edit_offer.html', context={'form': form})