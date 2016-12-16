from .models import Employees, Salaries, Titles
from rest_framework import serializers

class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = ('emp_no', 'birth_date', 'first_name', 'last_name', 'gender', 'hire_date')

class SalariesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Salaries
        fields = ('_id', 'emp_no', 'salary', 'from_date', 'to_date')

class TitlesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Titles
        fields = ('_id', 'emp_no', 'title', 'from_date', 'to_date')
