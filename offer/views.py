import logging

from django.shortcuts import render, redirect, get_object_or_404

from offer.forms import OfferForm, DeleteOfferForm
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
            offer = get_object_or_404(Offer, pk=offer_id)
            form = OfferForm(request.POST, instance=offer)
            form.save(commit=True)
            return redirect('/')
        else:
            offer = get_object_or_404(Offer, pk=offer_id)
            form = OfferForm(instance=offer)
    else:
        offer = get_object_or_404(Offer, pk=offer_id)
        form = OfferForm(instance=offer)

    return render(request=request, template_name='offer/edit_offer.html', context={'form': form})


def delete_offer(request, offer_id):
    """
    删除 offer 信息
    :param request:
    :param offer_id:
    :return:
    """
    offer = get_object_or_404(Offer, pk=offer_id)
    if request.method == 'POST':
        form = DeleteOfferForm(request.POST, instance=offer)

        if form.is_valid():
            offer.delete()
            return redirect('/')
        else:
            logging.error(form.errors)

    return redirect('/')
