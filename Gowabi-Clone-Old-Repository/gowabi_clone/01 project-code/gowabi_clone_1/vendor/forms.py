from django import forms
from .models import VendorProfile, ServiceListing

class VendorProfileForm(forms.ModelForm):
    class Meta:
        model = VendorProfile
        fields = ['business_name', 'contact_number', 'address']

class ServiceListingForm(forms.ModelForm):
    class Meta:
        model = ServiceListing
        fields = ['service', 'is_available', 'available_times']
