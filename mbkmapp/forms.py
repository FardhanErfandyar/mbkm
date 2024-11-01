from django.forms import ModelForm
from django import forms
from mbkmapp.models import *

class FormKonversi(ModelForm):
    class Meta:
        model = Konversi
        fields = ['matkul_konversi', 'ipk', 'document']
        labels = {
            'matkul_konversi': 'Mata Kuliah Konversi',
            'ipk': 'IPK',
            'document': 'Dokumen',
        }
        widgets = {
            'matkul_konversi': forms.TextInput(attrs={'class': 'form-control'}),
            'ipk': forms.NumberInput(attrs={'class': 'form-control'}),
            'document': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(FormKonversi, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = self.Meta.labels[field_name]


class FormSemester(ModelForm):
    dosen = forms.ModelChoiceField(queryset=Dosen.objects.all(), empty_label="Pilih Dosen Wali")
    class Meta:
        model = Mahasiswa
        fields = ['semester', 'dosen']
        labels = {
            'semester' : 'Semester',
            'dosen' : 'Dosen Wali'
            }
        widgets = {
            'semester': forms.TextInput(attrs={'class': 'form-control'}),
            'dosen': forms.Select(attrs={'class': 'form-control'}),

        }
    def __init__(self, *args, **kwargs):
        super(FormSemester, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = self.Meta.labels[field_name]