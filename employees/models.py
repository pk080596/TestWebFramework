from __future__ import unicode_literals

from django.db import models

class Employees(models.Model):
    emp_no = models.IntegerField(primary_key=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    hire_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'employees'
        verbose_name_plural = 'employees'


class Salaries(models.Model):
    _id = models.IntegerField(primary_key=True)
    emp_no = models.IntegerField()
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'salaries'
        verbose_name_plural = 'salaries'

class Titles(models.Model):
    _id = models.IntegerField(primary_key=True)
    emp_no = models.IntegerField()
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'titles'
        verbose_name_plural = 'titles'
