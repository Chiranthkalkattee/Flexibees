from django.contrib import admin
from .models import Candidate_feedback_report
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(Candidate_feedback_report)

class ViewAdmin(ImportExportModelAdmin):
    pass