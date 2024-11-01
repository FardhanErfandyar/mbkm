from django.shortcuts import render
from mbkmapp.forms import *

# Create your views here.


def landing(request):
    return render(request,"landing.html")

def download_form(request):
    return render(request,"form-download.html")

def form_konversi(request):
    form = FormKonversi()

    context = {
        'form':form,
    }

    return render(request, 'form-konversi.html', context)

def form_semester(request):
    form = FormSemester()

    context = {
        'form':form,
    }

    return render(request, 'form-semester.html', context)