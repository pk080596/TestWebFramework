from .models import Employees
from rest_framework import serializers

class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = ('emp_no', 'birth_date', 'first_name', 'last_name', 'gender', 'hire_date')
