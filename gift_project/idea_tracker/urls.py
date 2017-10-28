from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^forms/recipient_form/', views.recipient_form, name='recipient_form'),
    url(r'^forms/gift_form/', views.gift_form, name='gift_form'),
    url(r'^shoppinglist/', views.shopping_list, name='shopping_list'),
    url(r'^recipient_update/(?P<pk>\d+)/$', views.RecipientUpdate.as_view(), name='recipient_update_form'),
    url(r'^recipient_update/(?P<pk>\d+)/$', views.RecipientDelete.as_view()),
]

