from django.shortcuts import render
from employees.models import Employee
from django.http import Http404

# Create your views here.
def employee_detail(request, pk):
    try:
        employee = Employee.objects.get(pk = pk)
        print(employee)
    except:
        raise Http404("Employee does not exist")