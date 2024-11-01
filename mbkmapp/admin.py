from django.contrib import admin
from mbkmapp.models import *

# Register your models here.

class ProgramAdmin(admin.ModelAdmin):
    list_display = ['nama_program', 'penyelenggara', 'kuota']
    search_fields = ['nama_program', 'penyelenggara', 'kuota']  
    list_per_page = 8

admin.site.register(Program, ProgramAdmin)    