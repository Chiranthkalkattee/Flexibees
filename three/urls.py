from .views import Fetch_data
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('Fetch_data/', csrf_exempt(Fetch_data)),
    ]
