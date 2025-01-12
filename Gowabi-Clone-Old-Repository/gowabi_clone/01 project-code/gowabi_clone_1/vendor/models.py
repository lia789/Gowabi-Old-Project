from django.db import models
from django.contrib.auth.models import User
from booking.models import Service


class VendorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name





class ServiceListing(models.Model):
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    available_times = models.TextField(blank=True, null=True)  # Optional, for storing available times

    def __str__(self):
        return f"{self.vendor.business_name} - {self.service.name}"

