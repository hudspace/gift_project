from django.http import HttpResponse
from django.shortcuts import render

from .models import Recipient, Gift


def forms(request):
    return render(request, 'idea_tracker/forms.html', {'forms': forms})

def shoppinglist(request):
    return render(request, 'idea_tracker/shoppinglist.html')
