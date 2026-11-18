from django.core.management.base import BaseCommand
from config import WEBSITES

from testapp.validate_with_playwright import playwright_handler

class Command(BaseCommand):
    help="collect html and parse html using playwright and store the data in csv"

    def handle(self,*args,**options):
        results=[]

        for site_name,url in WEBSITES.items():

            if not url :
                self.stdout.write(self.style.WARNING(f"Skipping {site_name} :URL not configured"))
                continue
            
            self.stdout.write(f"Processing:{site_name}")
            result=playwright_handler(site_name,url)
            results.append(result)
    


            



