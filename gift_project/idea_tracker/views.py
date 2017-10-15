from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect


from . import forms
from . import models


def recipient_form(request):
    form = forms.RecipientForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.add_message(request, messages.SUCCESS, 'New gift recipient added!')
        return HttpResponseRedirect('/idea_tracker/forms/recipient_form')
    else:
        form = forms.RecipientForm()
    return render(request, 'idea_tracker/recipient_form.html', {'recipient_form': form})


def gift_form(request):
    form = forms.GiftForm(request.POST or None)
    print(form)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.add_message(request, messages.SUCCESS, 'New gift idea added!')
        return HttpResponseRedirect('/idea_tracker/forms/gift_form')
    else:
        form = forms.GiftForm()
    return render (request, 'idea_tracker/gift_form.html', {'gift_form': form})


def shopping_list(request, first_name):
    recipients = models.Recipient.objects.filter(first_name=first_name)
    return render(request, 'idea_tracker/shoppinglist.html', {'recipients': recipients, 'gifts': gifts, 'shoppingList': shoppingList})

def recipient_detail(request, first_name):
    recipients = models.Recipient.objects.filter(first_name=first_name)
    return render(request, 'idea_tracker/recipient_detail.html', {'first_name': first_name})

def recipient_edit(request):
    recipient = get_object_or_404(models.Recipient)
