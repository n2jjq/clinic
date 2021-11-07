from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Condition(models.Model):
  name = models.BooleanField(verbose_name='name',default=True)
  address = models.BooleanField(verbose_name='address',default=True)
  department = models.BooleanField(verbose_name='department',default=True)
  link = models.BooleanField(verbose_name='link',default=True)
  monday = models.BooleanField(verbose_name='monday',default=True)
  tuesday = models.BooleanField(verbose_name='tuesday',default=True)
  wednesday = models.BooleanField(verbose_name='wednesday',default=True)
  thursday = models.BooleanField(verbose_name='thursday',default=True)
  friday = models.BooleanField(verbose_name='friday',default=True)
  saturday = models.BooleanField(verbose_name='saturday',default=True)
  sunday = models.BooleanField(verbose_name='sunday',default=True)
  holiday = models.BooleanField(verbose_name='holiday',default=True)
  page = models.IntegerField(verbose_name='page', validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)

  def __str__(self):
    return '条件'