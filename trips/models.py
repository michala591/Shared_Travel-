from django.db import models

from locations.models import Locations
from users.models import User

"""
3.	Trips
o	Id (PK)
o	userID (FK - to Driver)
o	Days
o	Origin Station (fk location)
o	Destination Station (fk location) 
o	Departure Time
o	Return Time
"""


class Trips(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trips")
    days = models.CharField(max_length=50)
    departure_time = models.TimeField()
    return_time = models.TimeField()
    origin_station = models.ForeignKey(
        Locations, on_delete=models.CASCADE, related_name="trips_origin"
    )
    destination_station = models.ForeignKey(
        Locations, on_delete=models.CASCADE, related_name="trips_destination"
    )

    def __str__(self):
        return f"Trip by {self.user} from {self.origin_station} to {self.destination_station}"
