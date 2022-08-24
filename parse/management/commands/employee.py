from django.core.management.base import BaseCommand,CommandError
from ...models import Employee_details


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('Employee_name')
        parser.add_argument('Phone_number')
        parser.add_argument('Email')
        parser.add_argument('Designation')
        
       
    def handle(self, *args, **options):
        member =Employee_details(
            Employee_name = options['Employee_name'],
            Phone_number = options['Phone_number'],
            Email = options['Email'],
            Designation = options['Designation']
        )
        member.save()
        self.stdout.write(self.style.SUCCESS("Added"))
        