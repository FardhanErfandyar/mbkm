# Generated by Django 5.1.1 on 2024-10-31 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbkmapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='konversi',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='konversi',
            name='status',
            field=models.CharField(choices=[('sedang_diverifikasi', 'Sedang Diverifikasi'), ('diterima', 'Diterima'), ('ditolak', 'Ditolak')], default='sedang_diverifikasi', max_length=20),
        ),
    ]
