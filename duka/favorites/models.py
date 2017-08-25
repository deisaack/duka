from django.db import models
from duka.profiles.models import DataCollector

class PersonsFavorite(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	collector = models.ForeignKey(DataCollector, null=True, blank=True)
	CHILD = 0
	TEENAGER = 10
	TWENTIES = 20
	THIRTIES = 30
	FORTIES =40
	FIFTIES = 50
	SIXTIES = 60
	SEVENTIES = 70
	OLD = 80
	AGE_CHOICES = (('CHILD',CHILD),('TEENAGER',TEENAGER),('TWENTIES',TWENTIES),
	               ('THIRTIES',THIRTIES),('FORTIES',FORTIES),('FIFTIES',FIFTIES),
	               ('SIXTIES',SIXTIES),('SEVENTIES',SEVENTIES))
	age_bracket = models.SmallIntegerField(choices=AGE_CHOICES, null=True, blank=True)
