# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from animationfinder.models import Animation, Synonym



class SynonymAdmin(admin.ModelAdmin):

    model = Synonym
    list_display        = ['name', 'description', 'animations_list']
    readonly_fields     = ['animations_list']

    def animations_list(self, synonym):
        if synonym.animations:
            return ", ".join([animation.name for animation in synonym.animations.all()])
    animations_list.short_description = "Animation list"



admin.site.register(Animation)
admin.site.register(Synonym, SynonymAdmin)
