# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from animationfinder.models import Item, Animation, Description, Synonym


admin.site.register(Item)
admin.site.register(Animation)
admin.site.register(Description)
admin.site.register(Synonym)


