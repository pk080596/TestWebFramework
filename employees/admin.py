from django.contrib import admin
from .models import Employees, Salaries, Titles

models = [Employees, Salaries, Titles]

admin.site.register(models)
