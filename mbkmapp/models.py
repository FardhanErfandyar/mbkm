from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError


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


class Dosen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nip = models.CharField(max_length=50, unique=True)
    department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    office_address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.nip}"


class Mahasiswa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="profile_pictures/", null=True)
    universitas = models.CharField(max_length=100)
    nim = models.CharField(max_length=50)
    semester = models.IntegerField(null=True, blank=True)
    dosen = models.ForeignKey(Dosen, on_delete=models.SET_NULL, null=True, related_name="mahasiswa")

    def __str__(self):
        return self.user.username

def validate_ipk(value):
    if value < 0.0 or value > 4.0:
        raise ValidationError('IPK harus antara 0.0 hingga 4.0.')
    
class Konversi(models.Model):
    STATUS_CHOICES = [
        ('sedang_diverifikasi', 'Sedang Diverifikasi'),
        ('diterima', 'Diterima'),
        ('ditolak', 'Ditolak'),
    ]
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, null=True)  
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='sedang_diverifikasi')
    matkul_konversi = models.CharField(max_length=255)
    ipk = models.FloatField(validators=[validate_ipk])
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    dosen_wali = models.ForeignKey(Dosen, on_delete=models.SET_NULL, null=True, related_name="konversi_mahasiswa")
    
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, related_name="konversi_program")
    verifikasi = models.ForeignKey('Verifikasi', on_delete=models.SET_NULL, null=True, related_name="konversi")

    def __str__(self):
        return f"{self.id_konversi} - {self.mahasiswa.user.username} (Updated: {self.updated_at})"


class Verifikasi(models.Model):
    dosen_wali = models.ForeignKey(Dosen, on_delete=models.CASCADE, related_name='dosen_verifikasi')
    tanggal_verifikasi = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Konversi.STATUS_CHOICES)
    catatan = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Verifikasi oleh {self.dosen_wali.user.username} pada {self.tanggal_verifikasi}"
