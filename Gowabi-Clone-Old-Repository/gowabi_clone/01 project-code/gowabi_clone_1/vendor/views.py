from django.shortcuts import render, redirect, get_object_or_404
from .models import VendorProfile, ServiceListing
from django.contrib.auth.decorators import login_required
from .forms import VendorProfileForm, ServiceListingForm






@login_required
def dashboard(request):
    vendor = VendorProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = VendorProfileForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('vendor:dashboard')
    else:
        form = VendorProfileForm(instance=vendor)
    return render(request, 'vendor/dashboard.html', {'form': form})



@login_required
def vendor_services(request):
    vendor = VendorProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ServiceListingForm(request.POST)
        if form.is_valid():
            service_listing = form.save(commit=False)
            service_listing.vendor = vendor
            service_listing.save()
            return redirect('vendor:vendor_services')
    else:
        form = ServiceListingForm()
    services = ServiceListing.objects.filter(vendor=vendor)
    return render(request, 'vendor/vendor_services.html', {'form': form, 'services': services})

