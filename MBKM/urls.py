"""
URL configuration for MBKM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MBKM import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from mbkmapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name="landing"),
    path('programs/<int:id>/tambah-konversi/data-konversi', form_konversi, name="form_konversi"),
    path('programs/<int:id>/tambah-konversi/data-semester', form_semester, name="form_semester"),
    path('programs/<int:id>/tambah-konversi/download-form', download_form, name="download-form"),
    path('programs/<int:id>/tambah-konversi/status_daftar', status_daftar, name="status_daftar"),
    path('register-mahasiswa/', register_mahasiswa, name="register_mahasiswa"),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('programs/', daftar_program, name='daftar_program'),
    path('programs/<int:id>/', detail_program, name='detail_program'), 
    path('program-saya/', program_saya, name='program_saya'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)