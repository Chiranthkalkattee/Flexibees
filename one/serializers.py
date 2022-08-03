from rest_framework import serializers
from .models import Candidate_feedback_report


class Serializers(serializers.ModelSerializer):
    class Meta:
        model = Candidate_feedback_report
        fields = ["Client_name","Roles","BD_manager","Recruiter","candidate_name","selection"]