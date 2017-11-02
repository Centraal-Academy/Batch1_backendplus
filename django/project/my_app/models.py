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
        return "El programa es:" + {self.name}

class PersonQuerySet(models.QuerySet):
    def younger(self):
        return self.filter(age__lte=25)

    def older(self):
        return self.filter(age__gte=30)

class PersonManager(models.Manager):
    def get_queryset(self):
        return PersonQuerySet(self.model, using=self._db)

    def younger(self):
        return self.get_queryset().younger()

    def older(self):
        return self.get_queryset().older()

class Person(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255)
    program = models.ForeignKey(Program, related_name="program_person")
    age = models.IntegerField(default=0, help_text="solo numeros", validators=[validators.age_validation])

    objects = PersonManager()

    def __str__(self):
        return self.email

class EventPerson(models.Model):
    event = models.ForeignKey(Event, related_name="event_person")
    person = models.ForeignKey(Person, related_name="person_event")

    
