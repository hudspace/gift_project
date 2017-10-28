from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect


from . import forms
from . import models




def recipient_form(request):
    form = forms.RecipientForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
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
        instance = form.save()
        instance.save()
        messages.add_message(request, messages.SUCCESS, 'New gift idea added!')
        return HttpResponseRedirect('/idea_tracker/forms/gift_form')
    else:
        form = forms.GiftForm()
    return render (request, 'idea_tracker/gift_form.html', {'gift_form': form})


def shopping_list(request):
    recipients = models.Recipient.objects.prefetch_related('gift_set').all().order_by('last_name')
    gift_list = models.Gift.objects.all()
    total = []

    for y in gift_list:
        total.append(y.price)
        total_price = sum(total)
    return render(request, 'idea_tracker/shoppinglist.html', {'recipients': recipients, 'total_price': total_price})

#def recipient_detail(request, recipient_id):
    #recipient = get_object_or_404(models.Recipient, id=recipient_id)
    #return render(request, 'idea_tracker/recipient_detail.html', {'recipient': recipient})

class RecipientUpdate(UpdateView):
    model = models.Recipient
    fields = ['first_name', 'last_name', 'birthday', 'notes']
    template_name_suffix = '_update_form'
