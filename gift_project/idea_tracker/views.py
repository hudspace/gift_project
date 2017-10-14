from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect


from . import forms
from . import models


def recipient_form(request):
    form = forms.RecipientForm(request.POST or None)
    if form.is_valid():
        new_list = form.save(commit=False)
        new_list.save()
        messages.add_message(request, messages.SUCCESS, 'New gift recipient added!')
        return HttpResponseRedirect('/idea_tracker/forms/recipient_form')
    else:
        form = forms.RecipientForm()
    return render(request, 'idea_tracker/recipient_form.html', {'form': form})


def gift_form(request):
    form = forms.GiftForm(request.POST or None)
    print(form)
    if form.is_valid():
        new_item = form.save(commit=False)
        new_item.save()
        messages.add_message(request, messages.SUCCESS, 'New gift idea added!')
        return HttpResponseRedirect('/idea_tracker/forms/gift_form')
    else:
        form = forms.GiftForm()
    return render (request, 'idea_tracker/gift_form.html', {'form': form})


def shopping_list(request):
    recipients = models.Recipient.objects.order_by('first_name')
    gifts = models.Gift.objects.order_by('name')
    return render(request, 'idea_tracker/shoppinglist.html', {'recipients': recipients, 'gifts': gifts})

def recipient_detail(request):
    recipient = models.Recipient.objects.order_by('first_name')
    return render(request, 'idea_tracker/recipient_detail.html', {'recipient': recipient})
