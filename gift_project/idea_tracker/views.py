from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect


from . import forms
from . import models


class RecipientUpdate(UpdateView):
    model = models.Recipient
    fields = ['first_name', 'last_name', 'birthday', 'notes']
    template_name_suffix = '_update_form'


    def get_success_url(self):
        return reverse('shopping_list')


class RecipientDelete(DeleteView):
    model = models.Recipient

    def get_success_url(self):
        return reverse('shopping_list')


class GiftUpdate(UpdateView):
    model = models.Gift
    fields = ['name', 'model_number', 'price', 'recipients', 'purchased']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('shopping_list')


class GiftDelete(DeleteView):
    model = models.Gift

    def get_success_url(self):
        return reverse('shopping_list')


def recipient_form(request):
    form = forms.RecipientForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        messages.add_message(request, messages.SUCCESS, 'New gift recipient added!')
        return HttpResponseRedirect('/idea_tracker/forms/recipient_form/')
    else:
        form = forms.RecipientForm()
    return render(request, 'idea_tracker/recipient_form.html', {'recipient_form': form})


def gift_form(request):
    form = forms.GiftForm(request.POST or None)
    print(form)
    if form.is_valid():
        instance = form.save()
        instance.save()
        messages.add_message(request, messages.SUCCESS, 'New gift idea added!')
        return HttpResponseRedirect('/idea_tracker/forms/gift_form/')
    else:
        form = forms.GiftForm()
    return render (request, 'idea_tracker/gift_form.html', {'gift_form': form})


def shopping_list(request):
    #queryset that includes each object's associated gifts from Gift model(ManyToManyField)
    recipients = models.Recipient.objects.all().order_by('last_name')

    #queryset that will be iterated over in for loop below
    gift_list = models.Gift.objects.all()
    total = []
    total_price = 0

    #this loop sums the total of all gifts allowing a total starting budget to be displayed
    for y in gift_list:

        try:
            total.append(y.price)
            total_price = sum(total)

        except y.DoesNotExist:
            total_price -= y.price


    return render(request, 'idea_tracker/shoppinglist.html', {'recipients': recipients, 'total_price': total_price})
