# Generated by Django 4.0.6 on 2022-08-09 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=200)),
                ('Student_Regno', models.IntegerField(max_length=100)),
                ('Address', models.CharField(max_length=1000)),
                ('College_name', models.CharField(max_length=100)),
                ('Course', models.CharField(max_length=100)),
            ],
        ),
    ]
