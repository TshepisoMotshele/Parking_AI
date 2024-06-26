# system
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

def home(request):
    return HttpResponse("Welcome to the Smart AI Parking Solution")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('website/', include('website.urls')),
    path('api/', include('users.urls')),
    path('api/', include('vehicles.urls')),
    path('api/', include('payments.urls')),
    path('', home, name='home'), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
