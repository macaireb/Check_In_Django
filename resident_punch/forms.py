from django import forms
from .models import *


class CounselorForm(forms.ModelForm):
    class Meta:
        model = Counselor
        fields = ('first_name', 'last_name', 'floor')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Please Enter the Counselors first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Please Enter the Counselors last name'}),
        }


class EditCounselorForm(forms.ModelForm):
    class Meta:
        model = Counselor
        fields = ('first_name', 'last_name', 'floor')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Please Enter the Counselors first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Please Enter the Counselors last name'}),
        }


class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = ('first_name', 'last_name', 'counselor')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Please Enter the Residents first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Please Enter the Residents last name'}),
            'counselor': forms.Select(attrs={'class': 'form-control'}),
        }


class EditResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = ('first_name', 'last_name', 'counselor')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Please Enter the Residents first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Please Enter the Residents last name'}),
            'counselor': forms.Select(attrs={'class': 'form-control'}),
        }


class PunchForm(forms.ModelForm):
    class Meta:
        model = Punch
        fields = ('punch_in', 'resident')
        widgets = {
            'punch_in': forms.CheckboxInput(),
            'resident': forms.Select(attrs={'class': 'form-control'}),
        }