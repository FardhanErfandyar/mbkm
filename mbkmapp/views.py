from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404
from mbkmapp.forms import *

# Create your views here.


def landing(request):
    return render(request,"landing.html")

def daftar_program(request):
    programs = Program.objects.all() 
    return render(request, 'programs.html', {'programs': programs})

def register_mahasiswa(request):
    if request.method == 'POST':
        form = MahasiswaRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = MahasiswaRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('landing')  
            else:
                form.add_error(None, 'Username atau password salah.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def detail_program(request, id):
    program = get_object_or_404(Program, id=id)

    rincian_kegiatan_list = program.rincian_kegiatan.split(";")
    kriteria_peserta_list = program.kriteria_peserta.split(";")

    context = {
        'program': program,
        'rincian_kegiatan': rincian_kegiatan_list,
        'kriteria_peserta': kriteria_peserta_list,
    }
    return render(request, 'detail-program.html', context)

def form_semester(request, id):
    program = get_object_or_404(Program, id=id)
    
    mahasiswa = get_object_or_404(Mahasiswa, user=request.user)

    if request.method == "POST":
        form = FormSemester(request.POST, instance=mahasiswa)  
        if form.is_valid():
            form.save()  
            return redirect('download-form', id=program.id)  
    else:
        form = FormSemester(instance=mahasiswa)

    context = {
        'form': form,
        'program': program,  
    }

    return render(request, 'form-semester.html', context)

def download_form(request, id):
    program = get_object_or_404(Program, id=id)

    context = {
        'program': program,  
    }

    return render(request,"form-download.html", context)

def form_konversi(request, id):
    program = get_object_or_404(Program, id=id)
    mahasiswa = get_object_or_404(Mahasiswa, user=request.user)
    dosen_wali = mahasiswa.dosen

    if request.method == "POST":
        form = FormKonversi(request.POST, request.FILES) 
        if form.is_valid():
            konversi = form.save(commit=False)  
            konversi.program = program 
            konversi.dosen_wali = dosen_wali  
            konversi.mahasiswa = mahasiswa
            verifikasi = Verifikasi.objects.create(
                dosen_wali=dosen_wali,
                status=konversi.status, 
            )
            konversi.verifikasi = verifikasi
            konversi.save() 
            return redirect('status_daftar', id=konversi.id) 
    else:
        form = FormKonversi()

    context = {
        'form': form,
        'program': program,  
    }

    return render(request, 'form-konversi.html', context)


def status_daftar(request, id):
    konversi = get_object_or_404(Konversi, id=id)

    context = {
        'konversi': konversi,  
    }
    return render(request,"status.html", context)


def program_saya(request):
    mahasiswa = get_object_or_404(Mahasiswa, user=request.user)
    
    konversi_list = Konversi.objects.filter(mahasiswa=mahasiswa)

    context = {
        'konversi_list': konversi_list,
    }
    
    return render(request, 'program_saya.html', context)