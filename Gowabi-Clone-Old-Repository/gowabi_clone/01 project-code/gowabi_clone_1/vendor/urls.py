from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('services/', views.vendor_services, name='vendor_services'),
]
