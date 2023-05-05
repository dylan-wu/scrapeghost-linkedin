import os
from pprint import pprint
from scrapeghost import SchemaScraper, CSS
from linkedin_scraper import actions
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
actions.login(driver, username, password)

scrape_schema = SchemaScraper(
    schema={
        'person': 'string',
        'body': 'string',
        'duration': 'string'
    }
)

search_url = 'https://www.linkedin.com/feed/'
driver.get(search_url)

# Find all post postings on the page
posts = driver.find_elements(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div[3]/div')
posts_text = [post.get_attribute('outerHTML') for post in posts]
print(posts_text[0])

for html in posts_text:
    pprint(scrape_schema(html[:14000]))
