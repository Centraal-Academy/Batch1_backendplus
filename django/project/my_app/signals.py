from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from my_app import models

@receiver(pre_save, sender=models.Program)
def notification(sender, **kwargs):
    print(kwargs)
    


