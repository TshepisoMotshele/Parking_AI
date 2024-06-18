
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('start_parking/<str:license_plate_number>/', views.start_parking_session, name='start_parking_session'),
    path('end_parking/<str:license_plate_number>/', views.end_parking_session, name='end_parking_session'),
]