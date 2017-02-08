from __future__ import unicode_literals

from django.conf import settings

from django.db import models
from django.forms import ModelForm
from django import forms

class Image(models.Model):
	filename = models.CharField(max_length=50, unique=True)
