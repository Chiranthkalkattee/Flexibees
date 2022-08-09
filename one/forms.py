from django import forms
from .models import Candidate_feedback_report


class MyForm(forms.ModelForm):
    class Meta:
        model = Candidate_feedback_report
        fields = ["Client_name","Roles","BD_manager","Recruiter","candidate_name","selection"]
        labels = {'Client_name':"Client_name", "Roles": "Roles", "BD_manager": "BD_manager", "Recruiter": "Recruiter","candidate_name": "candidate_name", "selection": "selection"}

class SendMailForm(forms.Form):
    email_id = forms.EmailField()
    email_cc = forms.EmailField()
    email_bcc = forms.EmailField()
    subject = forms.CharField(max_length=200)
    msg = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField()