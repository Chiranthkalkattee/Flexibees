from django.shortcuts import render
from django.http import JsonResponse
from .models import student
# Create your views here.


def Fetch_data(request):
    data = list(student.objects.values())
    return JsonResponse(data,safe=False)

