from django.shortcuts import render
from employees.models import Employee
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def employee_detail(request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        return HttpResponse(employee)