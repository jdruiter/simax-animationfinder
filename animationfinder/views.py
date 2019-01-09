# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from joris.helperfunctions import safe_unicode as u
from joris.helperfunctions import select_words
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest, JsonResponse
import json

from animationfinder.models import Animation, Synonym


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
    http://localhost:8000/get-animations/{"sentence": "ducks"}
    '''

    if not json_sentence:
        return render(request, 'animationfinder/explanation.html')

    sentence = json.loads(json_sentence)['sentence']

    # parse the sentence
    word_list = select_words(sentence)

    result = {}
    for word in word_list:

        S = Synonym.objects.filter(name__iexact=word)
        animations = Animation.objects.filter(synonym__in=S)
        result[word] = [animation.name for animation in animations]

    return JsonResponse(result, safe=False)

