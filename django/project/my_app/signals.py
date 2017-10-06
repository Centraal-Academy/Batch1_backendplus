from django.db.models.signals import post_save
from django.dispatch import receiver
from my_app import models

@receiver(post_save, sender=models.Program)
def notification(sender, **kwargs):
    created = kwargs["created"]
    if created:
        print("Es nuevo registro")
    else:
        print("es actualizado")
    


