# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class NguoiDung(models.Model):
    uid = models.CharField(max_length=100)
    lastcontact= models.DateTimeField(auto_now_add=True)
    topic= models.CharField(max_length=100)
    status= models.IntegerField()

    def __unicode__(self):
        return self.uid