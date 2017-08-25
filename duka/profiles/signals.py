from django.db.models.signals import post_save
from django.dispatch import receiver
import logging
from . import models
from django.contrib.auth import get_user_model

logger = logging.getLogger("project")
User = get_user_model()


@receiver(post_save, sender=User)
def create_profile_handler(sender, instance, created, **kwargs):
    if not created:
        return
    # Create the profile object, only if it is newly created
    profile = models.DataCollector(user=instance)
    profile.save()
    logger.info('New user profile for {} created'.format(instance))

@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = models.DataCollector(user=user)
        profile.save()
