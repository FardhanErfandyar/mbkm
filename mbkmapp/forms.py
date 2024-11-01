from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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


class MahasiswaRegistrationForm(UserCreationForm):
    # Field tambahan untuk model Mahasiswa
    universitas = forms.CharField(max_length=100)
    nim = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(MahasiswaRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', 'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password', 'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password', 'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First Name', 'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last Name', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email', 'class': 'form-control'})
        self.fields['universitas'].widget.attrs.update({'placeholder': 'Universitas', 'class': 'form-control'})
        self.fields['nim'].widget.attrs.update({'placeholder': 'NIM', 'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Mahasiswa.objects.create(
                user=user,
                universitas=self.cleaned_data.get('universitas'),
                nim=self.cleaned_data.get('nim'),
            )
        return user
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')

    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username',
            'class': 'form-control'
        })
        self.fields['password'].widget.attrs.update({  
            'placeholder': 'Password',
            'class': 'form-control'
        })