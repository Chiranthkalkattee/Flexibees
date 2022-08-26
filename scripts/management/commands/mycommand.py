from django.core.management.base import BaseCommand,CommandError


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('first' , type=int, help="Integer values are accepted")
        parser.add_argument('--option1')

    def handle(self,*args,**options):
        # print('mycommand')
        # print(f'First:{options["first"]}')
        # print(f'option1:{options["option1"]}')
        

        if options['first'] % 2 == 0:
            self.stdout.write(self.style.SUCCESS('It is even number'))
        else:
            raise CommandError("odd number")
