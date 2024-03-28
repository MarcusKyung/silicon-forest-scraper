#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
positionsList = []

def main():
    print('---------------------------------')
    driver.get('https://www.thesiliconforest.com/oregon-tech-jobs')
    job_elems = driver.find_elements(By.CLASS_NAME, 'job-card-title')
    date_elems = driver.find_elements(By.CLASS_NAME, 'job-card-date')
    company_elems = driver.find_elements(By.CLASS_NAME, 'job-card-company-name')
    jobs = [elem.text for elem in job_elems]
    dates = [elem.text for elem in date_elems]
    companies = [elem.text for elem in company_elems]
    target_job_title = "Project Manager" 
    for job, date, company in zip(jobs, dates, companies):
        if job == target_job_title:
            print(f">>> Job: {color.YELLOW}{job}{color.END} - {company}\n>>> Date: {date}\n")
        else:
            print(f">>> Job: {job} - {company}\n>>> Date: {date}\n")
    print('---------------------------------')
    input("Press any key to close the browser...") 
    driver.quit()


main()