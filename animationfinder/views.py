# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from joris.helperfunctions import select_words
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
import json

from animationfinder.models import Item, Animation, Description, Synonym


def welcome(request):
    return render(request, 'animationfinder/explanation.html')


def get_animations(request, json_sentence=None):
    '''
    @json_sentence: a single sentence in a JSON
    Example: {"sentence": "We saw her duck. She loves ducks." }
    Returns A JSON object with animations mapped to words (words -> synonyms -> animations).
    Example:
    {
        word1: [Animation1, Animation2, …],
        word2: [Animation10, Animation100, …],
    }
    http://localhost:8000/get-animations/{"sentence": "test"}
    '''

    if not json_sentence:
        return render(request, 'animationfinder/explanation.html')

    try:
        sentence = json.loads(json_sentence)['sentence']
    except Exception as e:
        if type(json_sentence) == dict:
            sentence = json_sentence['sentence'].lowercase()
        else:
            return HttpResponseBadRequest("Please check your JSON is well formed")

    print sentence

    result = {}

    # alternatives: helperfunctions.select_words_unicode() and clear_interpunction()
    word_list = select_words(sentence)

    for word in word_list:
        try:    s = Synonym.objects.get(name__iexact=word)
        except: continue

        for description in s.description.all():
            item_list = []
            for item in description.item.all():
                print "'{}' matches animation: {}<br>".format(word, str(item.animation.pk))
                item_list.append(item.animation.pk)
            result[word] = item_list

    return JsonResponse(result, safe=False)

