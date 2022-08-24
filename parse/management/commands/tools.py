import logging
from django.core.management.base import BaseCommand
class DynamicCommand(BaseCommand):
    """
    When an arg is given after the management command this modified handle will automatically look for
    and call a method with that name.  Therefore, you can extend your management command Command() class
    from this class instead of Command and simple write functions that will be called by
    ./manage.py your_file_name your_function_name
    """
    def handle(self, *args, **kwargs):
        argument = args[:]
        extra_args = args[1:]
        if hasattr(self, argument):
            class_method = getattr(self, argument)
            class_method(extra_args) if extra_args else class_method()
        else:
            logging.error("No methods found that match the given args")