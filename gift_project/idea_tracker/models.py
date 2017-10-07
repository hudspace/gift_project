from django.core.urlresolvers import reverse
from django.db import models



class Recipient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.CharField(max_length=10)
    notes = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Gift(models.Model):
    name = models.CharField(max_length=30)
    model_number = models.CharField(max_length=30, blank=True)
    recipients = models.ManyToManyField(Recipient)

    def __str__(self):
        return "{}, {}".format(self.name, self.recipients)


