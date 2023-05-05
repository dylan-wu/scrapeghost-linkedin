import sys
import os
from pprint import pprint
from scrapeghost import SchemaScraper, CSS
from linkedin_scraper import actions
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib


driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
actions.login(driver, username, password)

scrape_schema = SchemaScraper(
    schema={
        'title': 'string',
        'company': 'string',
        'location': 'string',
        'duration': 'string'
    }
)

# Load the LinkedIn job search results page
search_term = 'Data Scientist'
location = 'Austin, Texas'
search_url = f'https://www.linkedin.com/jobs/search/?keywords={urllib.parse.quote(search_term)}&location={urllib.parse.quote(location)}&f_JIYN=true&refresh=true'
print(search_url)
driver.get(search_url)

# Find all job postings on the page
jobs = driver.find_elements(By.CSS_SELECTOR, 'li.jobs-search-results__list-item')
jobs_text = [job.text for job in jobs if job.text != '']

# Iterate over each job posting and extract relevant information
job_results = []
for job in jobs_text:
    job_elements = job.split('\n')
    job_results.append({'title': job_elements[0], 'company': job_elements[1], 'location': job_elements[2]})

print(job_results)

companies = set([job['company'] for job in job_results])
