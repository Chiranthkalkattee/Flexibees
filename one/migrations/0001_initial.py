# Generated by Django 4.0.6 on 2022-08-03 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate_feedback_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Client_name', models.CharField(max_length=22)),
                ('Roles', models.CharField(choices=[('Backend', 'Backend'), ('Frontend', 'Frontend'), ('QA', 'QA'), ('ProjectManager', 'ProjectManager'), ('Devops', 'Devops')], max_length=32)),
                ('BD_manager', models.CharField(default='Sonal', max_length=20)),
                ('Recruiter', models.CharField(default='goal', max_length=20)),
                ('candidate_name', models.CharField(max_length=30)),
                ('selection', models.CharField(max_length=30)),
            ],
        ),
    ]
