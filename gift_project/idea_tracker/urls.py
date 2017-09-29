from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^forms/', views.forms, name='forms'),
    url(r'^shoppinglist/', views.shoppinglist, name='shoppinglist')
]

