from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='Desciption default text')

    class Meta():
        db_table = "profile"

    def __unicode__(self):
        return self.name