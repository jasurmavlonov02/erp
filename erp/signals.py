from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Video


@receiver(post_save,sender = Video)
def update_status_to_ready(sender,instance,**kwargs):
    if instance.file:
        if instance.status == 'uploading':
            instance.status = 'ready'
            instance.save()