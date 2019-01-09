# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# word -> synoonyms -> animations

class Animation(models.Model):

    name = models.CharField(max_length=255, blank=False, unique=True)

    def __unicode__(self):
        return self.name


class Synonym(models.Model):

    name = models.CharField(max_length=255, blank=False, default='Synonym')
    description = models.CharField(max_length=255, blank=True)
    animations = models.ManyToManyField(Animation, blank=True)

    def __unicode__(self):
        return self.name
