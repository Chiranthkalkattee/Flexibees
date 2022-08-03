from django.db import models

# Create your models here.
class Candidate_feedback_report(models.Model):
    Role_choice=(('Backend','Backend'),
                 ('Frontend','Frontend'),
                 ('QA','QA'),
                 ('ProjectManager','ProjectManager'),
                 ('Devops','Devops'))

    Client_name=models.CharField(max_length=22)
    Roles=models.CharField(max_length=32,choices=Role_choice)
    BD_manager=models.CharField(max_length=20,default='Sonal')
    Recruiter=models.CharField(max_length=20,default='goal')
    candidate_name=models.CharField(max_length=30)
    selection=models.CharField(max_length=30)