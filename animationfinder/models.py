# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
    pass

class Animation(models.Model):
    item = models.OneToOneField(Item, primary_key=True, blank=False)

class Description(models.Model):
    item = models.ManyToManyField(Item, blank=True)

class Synonym(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True, default='Synonym')
    description = models.ManyToManyField(Description, blank=False)

    def __unicode__(self):
        return self.name
