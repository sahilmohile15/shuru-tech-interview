from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Matches(models.Model):
    id = models.AutoField(primary_key=True)
    date_of_match = models.DateField()
    venue = models.CharField(max_length=512)
    player_of_match = models.CharField(max_length=256)
    teams = models.ManyToManyField('Teams', blank=True)
    declared = models.BooleanField(default=True)
    
    def __str__(self):
        return (self.date_of_match.strftime('%Y-%m-%d') + self.venue)
    
class Teams(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512)
    wins = models.IntegerField()
    losses = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Players(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    team = models.ForeignKey(Teams, null=True,on_delete=models.SET_NULL)