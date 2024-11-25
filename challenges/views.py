from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect,Http404
from django.urls import reverse
from django.shortcuts import render
from django.template.loader import render_to_string

monthly_challenges = {
    "january": 'Drink 3l of water everyday',
    "february": 'Drink 3l of water everyday',
    "march": '0 chicken month',
    'april': '1 chicken',
    'may': '12 chicken salads this month',
    'june': '2 chicken month',
    'july': "3 chicken",
    'august': '4 chicken',
    'september': '5 apples per day',
    'october': '6 apples per day',
    'november': '7 apples per day',
    'december': None

}


# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{
        "months": months,
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('Invalid month')

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'text': challenge_text, 'month_name': month
        })
    except:
        raise Http404()
