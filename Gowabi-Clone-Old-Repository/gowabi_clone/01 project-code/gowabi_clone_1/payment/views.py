from django.shortcuts import render, get_object_or_404, redirect
from .models import Payment
from booking.models import Appointment
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        payment = Payment.objects.create(
            appointment=appointment,
            amount=appointment.service.price,
            payment_method='Credit Card',  # This is just an example
            status='completed'
        )
        return redirect('payment:confirmation', payment_id=payment.id)
    return render(request, 'payment/checkout.html', {'appointment': appointment})

@login_required
def payment_history(request):
    payments = Payment.objects.filter(appointment__user=request.user.customerprofile)
    return render(request, 'payment/payment_history.html', {'payments': payments})
