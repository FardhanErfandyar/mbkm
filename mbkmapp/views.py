from django.shortcuts import render

# Create your views here.


def landing(request):
    render(request, "landing.html")