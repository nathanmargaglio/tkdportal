from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group


class Income(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    school = models.CharField(max_length=128, default=None, null=True)
    date = models.DateTimeField(default=None, null=True)
    check = models.CharField(max_length=128, default=None, null=True)
    cash = models.CharField(max_length=128, default=None, null=True)
    credit_card = models.CharField(max_length=128, default=None, null=True)
    vending = models.CharField(max_length=128, default=None, null=True)
    ez_payment = models.CharField(max_length=128, default=None, null=True)

    def __str__(self):
        return "Created: " + str(self.created)
