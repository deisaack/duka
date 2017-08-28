from django.db import models
from duka.profiles.models import Collector
from geoposition.fields import GeopositionField
from django.urls import reverse
from django.utils.text import slugify
class BaseModels(models.Model):
	created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated = models.DateTimeField(auto_now=True, null=True, blank=True)

	class Meta:
		abstract = True


class Drink(BaseModels):
	name = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(editable=False, unique=True, null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('favorites:drink_detail', kwargs={'slug': self.slug})

	def create_slug(instance, x=2, new_slug=None, ):
		slug = slugify(instance.name)
		if new_slug is not None:
			slug = new_slug
		qs = Drink.objects.filter(slug=slug).order_by('-id')
		exists = qs.exists()
		if exists:
			slug = '%s-%s' % (slugify(instance.name), x)
			x += 1
			return Drink.create_slug(instance, x=x, new_slug=slug)
		return slug

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = Drink.create_slug(self)
			super(Drink, self).save(*args, **kwargs)
		if not self.slug:
			self.slug = Drink.create_slug(self)
		super(Drink, self).save(*args, **kwargs)


class Favorite(BaseModels):
	name = models.CharField(max_length=50, null=True, blank=True)
	collector = models.ForeignKey(Collector, null=True, blank=True)
	CHILD = '<<10'
	TEENAGER = '10-20'
	TWENTIES = '20-30'
	THIRTIES = '30-40'
	FORTIES = '40-50'
	FIFTIES = '50-60'
	SIXTIES = '60-70'
	OLD = '70>>'
	AGE_CHOICES = [(CHILD,'CHILD'),(TEENAGER,'TEENAGER'),(TWENTIES,'TWENTIES'),
				   (THIRTIES,'THIRTIES'),(FORTIES,'FORTIES'),(FIFTIES,'FIFTIES'),
				   (SIXTIES,'SIXTIES'),(OLD, 'OLD')]
	age_bracket = models.CharField(max_length=5, choices=AGE_CHOICES, null=True, blank=True)
	location = GeopositionField(null=True, blank=True)
	drink = models.ForeignKey(Drink, null=True, blank=True)
	slug = models.SlugField(editable=False, unique=True)

	class Meta:
		verbose_name = 'Person\'s Favourite'
		verbose_name_plural = 'People\'s Favourite'

	def __str__(self):
		return ('%s' % (self.name))

	def create_slug(instance, x=2, new_slug=None, ):
		slug = slugify(instance.name)
		if new_slug is not None:
			slug = new_slug
		qs = Favorite.objects.filter(slug=slug).order_by('-id')
		exists = qs.exists()
		if exists:
			slug = '%s-%s' % (slugify(instance.name), x)
			x += 1
			return Favorite.create_slug(instance, x=x, new_slug=slug)
		return slug

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = Favorite.create_slug(self)
			super(Favorite, self).save(*args, **kwargs)
		if not self.slug:
			self.slug = Favorite.create_slug(self)
		super(Favorite, self).save(*args, **kwargs)


	def get_absolute_url(self):
		return reverse('favorites:favorite_detail', kwargs={'slug': self.slug})
