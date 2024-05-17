import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")

"""
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
"""
    
class Scrape:

    def __init__(self):
        """Initializes the scrape option"""
  


    def gettitle(self):
        """Returns the Title of all the jobs on the website"""
        for job_element in job_elements:
            title_element = job_element.find("h2", class_="title")
            titlenum = print("\n",title_element.text.strip())
            
        
    def getcompany(self):
        """Returns the company of each worker on the website"""
        for job_element in job_elements:
            company_element = job_element.find("h3", class_="company")
            companynum = print("\n",company_element.text.strip())
            
        
    def getlocation(self):
        """Returns the Location of all the workers on the website"""
        for job_element in  job_elements:
            location_element = job_element.find("p", class_="location")
            locationnum = print("\n",location_element.text.strip())
            
