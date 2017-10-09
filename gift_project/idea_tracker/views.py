from django.contrib import messages
from django.shortcuts import get_object_or_404, render


from . import forms
from . import models


def recipient_form(request):
    recipient_form = forms.RecipientForm()
    if recipient_form.is_valid():
        new_list = form.save(commit=False)
        new_list.save()
        messages.add_message(request, messages.SUCCESS, 'New gift recipient list added!')
    return render(request, 'idea_tracker/recipient_form.html', {'recipient_form': recipient_form})

def gift_form(request):
    gift_form = forms.GiftForm()
    if gift_form.is_valid():
        new_item = form.save(commit=False)
        new_item.save()
        messages.add_message(request, messages.SUCCESS, 'New gift idea added!')
    return render (request, 'idea_tracker/gift_form.html', {'gift_form': gift_form})


def shopping_list(request):
    return render(request, 'idea_tracker/shoppinglist.html', {'shopping_list': shopping_list})
