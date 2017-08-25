from django.db import models
from django.conf import settings
from geoposition.fields import GeopositionField
from django.core.urlresolvers import reverse


class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = GeopositionField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("academics:timetable-item", kwargs={"slug": self.name})


class DataCollector(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    collector_no = models.CharField(max_length=20, unique=True, null=True, blank=True)
    id_no = models.IntegerField(null=True, blank=True, unique=True)
    dob = models.DateField(null=True, blank=True)
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (('m', MALE), ('f', FEMALE))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    centre = models.ForeignKey(Location, null=True, blank=True)

    class Meta:
        verbose_name= 'Data Collector'
        verbose_name_plural = 'Data Collectors'


    def __str__(self):
        return self.collector_no
