'''from django import forms

class FileUploadForm(forms.Form):
    csv_file = forms.FileField()
'''
# store/forms.py

from django import forms
from .models import PatientProfile

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = '__all__'