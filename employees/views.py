from .models import Employees, Salaries, Titles
from rest_framework import viewsets
from .serializers import EmployeesSerializer, SalariesSerializer, TitlesSerializer

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all().order_by('emp_no')
    serializer_class = EmployeesSerializer

class SalariesViewSet(viewsets.ModelViewSet):
    queryset = Salaries.objects.all().order_by('_id')
    serializer_class = SalariesSerializer
    
class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all().order_by('_id')
    serializer_class = TitlesSerializer
