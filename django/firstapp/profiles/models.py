from __future__ import unicode_literals
from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(default='location', max_length=120)
    description = models.TextField(default='Description default text')
    job = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        db_table = "profile"

    @property
    def __unicode__(self):
        return self.name