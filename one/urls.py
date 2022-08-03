from .views import Candidate_report,Candidate_list,export_to_csv
from django.urls import path

urlpatterns = [
    path('can/',Candidate_report),
    path('details/',Candidate_list),
    path('download/',export_to_csv)
]