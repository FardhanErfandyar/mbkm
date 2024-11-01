from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Program(models.Model):
    nama_program = models.CharField(max_length=255)
    penyelenggara = models.CharField(max_length=255)
    durasi = models.CharField(max_length=64)
    kuota = models.PositiveIntegerField()
    deskripsi = models.TextField()
    rincian_kegiatan = models.TextField()
    kriteria_peserta = models.TextField()
    sks = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama_program 


class Konversi(models.Model):
    STATUS_CHOICES = [
        ('sedang_diverifikasi', 'Sedang Diverifikasi'),
        ('diterima', 'Diterima'),
        ('ditolak', 'Ditolak'),
    ]
    
    id_konversi = models.CharField(max_length=255)  
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='sedang_diverifikasi') 
    matkul_konversi = models.CharField(max_length=255)
    ipk = models.FloatField()
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    def __str__(self):
        return f"{self.id_konversi} (Updated: {self.updated_at})"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="profile_pictures/", null=True)
    universitas = models.CharField(max_length=100)  
    nim = models.CharField(max_length=50)          
    semester = models.IntegerField(null=True, blank=True)  

    def __str__(self):
        return self.user.username
