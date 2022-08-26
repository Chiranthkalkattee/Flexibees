from django.contrib import admin
from django.urls import path
from .views import export_to_csv,export_to_csv1
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('download/',export_to_csv),
    path('newemp/',export_to_csv1)
]
