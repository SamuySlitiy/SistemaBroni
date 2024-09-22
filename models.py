from django.db import models
from django.contrib.auth.models import User

class Section(models.Model):
    number = models.IntegerField()

class Table(models.Model):
    is_free = models.BooleanField(default=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

class Booking(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    taken_table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateTimeField() 
    confirmation = models.BooleanField(default=True)

# Create your models here.