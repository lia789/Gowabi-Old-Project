from django.shortcuts import render, redirect
from .models import CustomerProfile
from booking.models import Appointment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomerProfileForm







@login_required
def profile_view(request):
    profile = CustomerProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user:profile_view')
    else:
        form = CustomerProfileForm(instance=profile)
    return render(request, 'user/profile_view.html', {'form': form})



@login_required
def booking_history(request):
    appointments = Appointment.objects.filter(user=request.user.customerprofile)
    return render(request, 'user/booking_history.html', {'appointments': appointments})
