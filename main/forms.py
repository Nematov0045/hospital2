from django import forms
from .models import Hospital, MainDoctor,Nurses, Patient,Doctor

class AddPatient(forms.ModelForm):
    class Meta:
        model=Patient
        fields='__all__'
class AddNurses(forms.ModelForm):
    class Meta:
        model=Nurses
        fields='__all__'
class AddMainDoctor(forms.ModelForm):
    class Meta:
        model=MainDoctor
        fields='__all__'
class AddDoctor(forms.ModelForm):
    class Meta:
        model=Doctor
        fields='__all__'       

