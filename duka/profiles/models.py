from django.db import models
from django.conf import settings
from django.utils.text import slugify
from geoposition.fields import GeopositionField
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from duka.storage_backends import PrivateMediaStorage


class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()


class PrivateDocument(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(storage=PrivateMediaStorage())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='documents')

class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = GeopositionField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("academics:timetable-item", kwargs={"slug": self.name})


class Collector(models.Model):
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
    slug = models.SlugField(unique=True, editable=False)

    class Meta:
        verbose_name= 'Data Collector'
        verbose_name_plural = 'Data Collectors'

    def create_slug(instance, x=2, new_slug=None, ):
        slug = slugify(instance.collector_no)
        if new_slug is not None:
            slug = new_slug
        qs = Collector.objects.filter(slug=slug).order_by('-id')
        exists = qs.exists()
        if exists:
            slug = '%s-%s' % (slugify(instance.collector_no), x)
            x += 1
            return Collector.create_slug(instance, x=x, new_slug=slug)
        return slug

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = Collector.create_slug(self)
            super(Collector, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = Collector.create_slug(self)
        super(Collector, self).save(*args, **kwargs)

    def __str__(self):
        return ('Collector %s (%s)' % (self.user.name, self.user.email))


    def get_absolute_url(self):
        return reverse("profiles:collector_detail", kwargs={"slug": self.slug})
