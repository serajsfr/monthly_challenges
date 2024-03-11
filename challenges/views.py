from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Read books more often!",
    "february": "Learn a new framework!",
    "march": "Exercise more!",
    "april": "Read books more often!",
    "may": "Learn a new framework!",
    "june": "Exercise more!",
    "july": "Learn a new framework!",
    "august": "Read books more often!",
    "september": "Exercise more!",
    "october": "Read books more often!",
    "november": "Learn a new framework!",
    "december": None,
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenges.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        raise Http404()
    
