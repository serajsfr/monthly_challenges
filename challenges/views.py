from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "december": "Read books more often!",
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #challenge/january
    return HttpResponseRedirect(redirect_path)

def january(request):
    return HttpResponse("Read books more often!")

def february(request):
    return HttpResponse("Learn a new framework!")

def march(request):
    return HttpResponse("Exercise more!")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    
