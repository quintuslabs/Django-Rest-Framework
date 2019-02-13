from time import timezone

from django.db import models

# Create your models here.


class Employee(models.Model):
    Gender_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    name = models.CharField(max_length=200, blank=True, default='')
    phone = models.CharField(max_length=10, blank=False)
    gender = models.CharField(max_length=10, choices=Gender_CHOICES, blank=True, default='')
    image = models.FileField(upload_to='images', blank=True, default='')
    height = models.CharField(max_length=5, blank=True, default='')
    weight = models.CharField(max_length=5, blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'