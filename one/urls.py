from .views import Candidate_report,Candidate_list,export_to_csv,simple_send_mail,thank_you
from django.urls import path

urlpatterns = [
    path('can/',Candidate_report),
    path('details/',Candidate_list),
    path('download/',export_to_csv),
    path('sendemail/', simple_send_mail, name='emailattachment'),
    path('mail/thanks/',thank_you)
]