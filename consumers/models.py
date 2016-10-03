from django.db import models
from tours.models import Tour


class Consumer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return u'{}, {}, {}, {}'.format(self.name,self.surname,self.email, self.phone)


class Booking(models.Model):
    status = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    fin_date = models.DateTimeField()
    consumer = models.ForeignKey(Consumer, null=True)
    tour = models.ForeignKey(Tour, null=True)

    def __str__(self):
        return u'{}, {}, {}, {}, {}'.format(self.status,self.start_date,self.fin_date, self.consumer,
                                            self.tour)


