from django.urls import reverse
from django.db import models


class Recipient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.CharField(max_length=10, blank=True)
    notes = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('recipient_update_form', kwargs={'pk': self.pk})


class Gift(models.Model):
    name = models.CharField(max_length=30, blank=True)
    model_number = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=6)
    recipients = models.ManyToManyField(Recipient, blank=True)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse('gift_update_form', kwargs={'pk': self.pk})
