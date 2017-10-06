from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import validators

# Create your models here.
class Meetup(models.Model):
    name = models.CharField(max_length=50, help_text="Max length 50")
    logo = models.ImageField(null=True)

class Event(models.Model):
    name = models.CharField(max_length=200, help_text="Max length 200")
    date = models.DateField(auto_now=False, help_text="format dd-mm-yyyy", error_messages={"message":"Plese put a valid date"}, validators= [validators.validate_date_event])
    time = models.TimeField(auto_now=False)
    confirmed = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=50)
    instructor = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"El programa es: {self.name}"

class Person(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255)
    program = models.ForeignKey(Program, related_name="program_person")
    age = models.IntegerField(default=0, help_text="solo numeros", validators=[validators.age_validation])

    def __str__(self):
        return self.email


    
