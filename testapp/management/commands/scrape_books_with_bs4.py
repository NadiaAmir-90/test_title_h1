from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from testapp.validate_with_bs4 import handler
from testapp.report import generate_csv
from config import BOOKS_WEBSITE

class Command(BaseCommand):
    help="collect html and parse html using BS4 and store the data in csv"

    def handle(self,*arg,**options):
        results=[]

        for site_name,url in BOOKS_WEBSITE.items():

            if not url :
                self.stdout.write(self.style.WARNING(f"Skipping {site_name} :URL not configured"))
                continue
            
            self.stdout.write(f"Processing:{site_name}")
            result=handler(site_name,url)
            results.append(result)
        
        if results:
            validate_data(results)
            generate_csv(results)
            
        else:
            self.stdout.write(self.style.WARNING("No results available to export."))


            



