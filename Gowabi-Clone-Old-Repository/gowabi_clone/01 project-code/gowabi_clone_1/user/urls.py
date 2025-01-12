from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile_view'),
    path('history/', views.booking_history, name='booking_history'),
]
