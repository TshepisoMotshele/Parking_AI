# website/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from .models import User, ParkingSession
from .models import Profile, Vehicle

from rest_framework import viewsets
from .models import Profile, Vehicle
from .serializers import ProfileSerializer, VehicleSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer                                                                

def register_user(request):
    print("Inside register_user view")
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = UserRegistrationForm()
    return render(request, 'website/register_user.html', {'form': form})

def registration_success(request):
    return HttpResponse("Registration successful!")

def start_parking_session(request, license_plate_number):
    try:
        user = User.objects.get(license_plate_number=license_plate_number)
        session = ParkingSession(user=user)
        session.save()
        return HttpResponse(f"Parking session started for {license_plate_number}")
    except User.DoesNotExist:
        return HttpResponse("User not found!")

def end_parking_session(request, license_plate_number):
    try:
        user = User.objects.get(license_plate_number=license_plate_number)
        session = ParkingSession.objects.filter(user=user, end_time__isnull=True).first()
        if session:
            session.end_session()
            cost = session.calculate_cost()
            return HttpResponse(f"Parking session ended for {license_plate_number}. Total cost: R{cost}")
        else:
            return HttpResponse("No active parking session found!")
    except User.DoesNotExist:
        return HttpResponse("User not found!")
