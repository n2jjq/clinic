from django.db import models

class Condition(models.Model):
  name = models.BooleanField(verbose_name='',default=True)
  address = models.BooleanField(verbose_name='',default=True)
  department = models.BooleanField(verbose_name='',default=True)
  monday = models.BooleanField(verbose_name='',default=True)
  tuesday = models.BooleanField(verbose_name='',default=True)
  wednesday = models.BooleanField(verbose_name='',default=True)
  thursday = models.BooleanField(verbose_name='',default=True)
  friday = models.BooleanField(verbose_name='',default=True)
  thursday = models.BooleanField(verbose_name='',default=True)
  sunday = models.BooleanField(verbose_name='',default=True)
  holiday = models.BooleanField(verbose_name='',default=True)