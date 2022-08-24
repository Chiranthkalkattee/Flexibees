from django.contrib import admin
from django.urls import path
from .views import export_to_csv
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('download/',export_to_csv)
]
