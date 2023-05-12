from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from attence.models import Employee
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404, JsonResponse

def check_in(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    employee.check_in = timezone.now()
    employee.save()
    return render(request, 'attendance/check_in.html', {'employee': employee})

def check_out(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    employee.check_out = timezone.now()
    employee.save()
    return render(request, 'attendance/check_out.html', {'employee': employee})
