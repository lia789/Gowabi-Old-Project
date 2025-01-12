from django.db import models
from booking.models import Appointment

class Payment(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)  # e.g., 'Credit Card', 'Paypal'
    status = models.CharField(max_length=20, choices=[('completed', 'Completed'), ('failed', 'Failed'), ('pending', 'Pending')], default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.appointment} - {self.status}"



class PaymentHistory(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"PaymentHistory for {self.payment} - {self.status} at {self.timestamp}"



