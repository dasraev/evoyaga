from django.core.management.base import BaseCommand
from juvenile.models import *
from datetime import datetime
import xlwt
from scripts.some_data import export_juvenile_data

class Command(BaseCommand):
    help = 'Export juvenile data to Excel'

    def handle(self, *args, **kwargs):
        export_juvenile_data()
        self.stdout.write('Juvenile data exported successfully.')
