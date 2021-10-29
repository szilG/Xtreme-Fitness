from django.shortcuts import render
from django.contrib import messages
from .forms import SubscriberForm


def add_subscribe(request, template='subscribe/subscribe.html'):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            form = SubscriberForm()
            messages.success(request, 'Successfully Subscribed!')
        else:
            messages.error(request, 'Failed to subscribe.')
    else:
        form = SubscriberForm()

    template = 'subscribe/subscribe.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
