from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, Appointment
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import AppointmentForm



def service_list(request):
    services = Service.objects.all()
    return render(request, 'booking/service_list.html', {'services': services})


def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'booking/service_detail.html', {'service': service})




@login_required
def book_appointment(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user.customerprofile
            appointment.service = service
            appointment.save()
            return redirect('booking:confirmation', appointment_id=appointment.id)
    else:
        form = AppointmentForm()
    return render(request, 'booking/book_appointment.html', {'service': service, 'form': form})

