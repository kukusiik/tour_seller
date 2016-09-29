from django.db import models

from airlines.models import Airline
from tourOperators.models import TourOperator
from places.models import Hotel
from places.models import City
from consumers.models import Booking


class Tour(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    startDate = models.DateTimeField()
    finDate = models.DateTimeField()
    airline = models.ForeignKey(Airline)
    tourOperator = models.ForeignKey(TourOperator)
    capacity = models.PositiveIntegerField()
    destination = models.ForeignKey(Hotel)
    departureCity = models.ForeignKey(City)
    booking = models.ForeignKey(Booking)



def __str__(self):
    return '{} ({:%Y-%m-%d} - {:%Y-%m-%d})'.format(
        self.name, self.start, self.end)





