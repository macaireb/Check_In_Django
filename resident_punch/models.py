from django.db import models
from django.db.models.functions import Now
from django.urls import reverse
# Create your models here.


class Counselor(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    floor = models.IntegerField(default=4)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('home')


class Resident(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    floor = models.IntegerField(default=4)
    title_tag = models.CharField(max_length=100)
    counselor = models.ForeignKey(Counselor, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('resident_detail', args=str(self.id))


class Punch(models.Model):
    time = models.DateTimeField("Time of punch", default=Now())
    punch_in = models.BooleanField(default=False, blank=False)
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)

    def __str__(self):
        return self.time

    def get_absolute_url(self):
        return reverse('home')