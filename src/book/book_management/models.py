from django.db import models
import uuid
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


class Pet(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)


    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)




