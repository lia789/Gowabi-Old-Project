from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    appointment_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Appointment
        fields = ['appointment_time']
