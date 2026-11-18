import csv
from config import REPORT_DIR

def generate_csv(results):
    """generate a csv report from parse data"""
    
    csv_file=REPORT_DIR/"results.csv"

    # define the csv file column
    fieldnames = [
        "site_name",
        "url",
        "bs4_title",
        "bs4_h1",
    ]
    with open(csv_file,"w",newline="",encoding="utf-8-sig") as file:
        
        writer=csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    return csv_file