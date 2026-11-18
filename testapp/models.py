from django.db import models

class Results(models.Model):

    site_name = models.CharField(max_length=100)
    bs4_title=models.CharField(max_length=100)
    playwright_title=models.CharField(max_length=100)
    title_passed = models.BooleanField(default=False)
    bs4_h1=models.CharField(max_length=100)
    playwright_h1=models.CharField(max_length=100)
    h1_passed= models.BooleanField(default=False)
    

    class Meta:
        verbose_name = "Result"
    def __str__(self):
      return f"{self.site_name} - Title: {self.title_passed}, H1: {self.h1_passed}"

