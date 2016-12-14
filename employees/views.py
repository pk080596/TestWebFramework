from .models import Employees
from rest_framework import viewsets
from .serializers import EmployeesSerializer

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all().order_by('emp_no')
    serializer_class = EmployeesSerializer
    


