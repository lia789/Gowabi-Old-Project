from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)  # e.g., 'Massage', 'Facial'
    available_slots = models.IntegerField(default=0)  # Number of available time slots for booking

    def __str__(self):
        return self.name



class Appointment(models.Model):
    user = models.ForeignKey('user.CustomerProfile', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('booked', 'Booked'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='booked')

    def __str__(self):
        return f"Appointment for {self.user} - {self.service.name} on {self.appointment_time}"


