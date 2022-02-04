from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    return render(request, "age/index.html")

def age_teller(request):
    if request.method == "POST":
        day = request.POST.get("day", "")
        month = request.POST.get("month", "")
        year = request.POST.get("year", )
        x = datetime.datetime.now()
        current_day = int(x.day) - int(day)
        current_month = int(x.month) - int(month)
        current_year = int(x.year) - int(year)




        return render(request, "age/basic.html",{"day": abs(int(current_day)), "month": abs(int(current_month)), "year": abs(int(current_year))})
