from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import render


# Create your views here.

def january(request):
    return HttpResponse("Drink 3l of water everyday")


def february(request):
    return HttpResponse("0 chicken month")


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'Drink 3l of water everyday'
    elif month == 'february':
        challenge_text = '0 chicken month'
    elif month == 'march':
        challenge_text = 'Eat at least 5000kcal a day'
    else:
        return HttpResponseNotFound('This month is not supported')

    return HttpResponse(challenge_text)
