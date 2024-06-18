# system
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Smart AI Parking Solution")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('website/', include('website.urls')),
    path('', home, name='home'), 
]
