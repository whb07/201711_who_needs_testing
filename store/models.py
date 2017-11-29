from django.db import models
# Create your models here.


class Vacation(models.Model):
    # CABIN IN PLANE
    CHEAP = 'ECONOMY'
    FIRST = 'FIRST'
    CABIN_CHOICES = (
        (CHEAP, 'Economy: Save Money!'),
        (FIRST, 'First Class: Travel In Luxury'),
    )
    # CITIES TO PICK
    PARIS = 'PARIS'
    LONDON = 'LONDON'
    BALI = 'BALI'
    CITIES = (
        (PARIS, 'Paris: City of Light'),
        (LONDON, 'London: Fish & Chips!'),
        (BALI, 'Bali: Relax!'),
    )
    city = models.CharField(max_length=25, choices=CITIES, default=LONDON)
    created = models.DateTimeField(auto_now_add=True)
    travelers = models.IntegerField()
    cabin = models.CharField(max_length=25, choices=CABIN_CHOICES)
    start_travel = models.DateTimeField()
    end_travel = models.DateTimeField()
