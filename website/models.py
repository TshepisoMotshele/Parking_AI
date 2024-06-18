from django.db import models
from django.utils import timezone

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    license_plate_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.license_plate_number}"

class ParkingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def end_session(self):
        self.end_time = timezone.now()
        self.save()

    def get_duration(self):
        if self.end_time:
            return self.end_time - self.start_time
        return timezone.now() - self.start_time

    def calculate_cost(self):
        duration = self.get_duration()
        # Assuming the rate is R5 per hour
        hours = duration.total_seconds() / 3600
        return round(hours * 5, 2)

    def __str__(self):
        return f"Session for {self.user.license_plate_number} started at {self.start_time}"