"""
Name: Kris Karciauskas
Final project for Computer Programming 2
"""

import requests
from bs4 import BeautifulSoup
"""
URL = "https://realpython.github.io/fake-jobs/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")


job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
"""

# find the code in the body portion of the page and find a way to convert it all into text, while avoiding all the links that pop up, as well
# as random advertisements and such, fillers of the page to say

URL = 'https://realpython.com/beautiful-soup-web-scraper-python/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id=True)
elements = results.find_all("div", class_="main-content")


for i in elements:
    pagetxt = i.find("p")
    print(pagetxt.text.strip())
    print()