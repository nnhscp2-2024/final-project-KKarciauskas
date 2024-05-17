"""
Name: Kris Karciauskas
Final project for Computer Programming 2
"""

from scrapes import Scrape
scrape1 = Scrape()
while True:
    userchoice = int(input("""\nWhat would you like to find?
                   0: I'm Done!
                   1: Job Title
                   2: Company
                   3: Location
                   Your Choice: """))
    if userchoice != -1:
        if userchoice == 0:
            break
        if userchoice == 1:
            scrape1.gettitle()
        elif userchoice == 2:
            scrape1.getcompany()
        elif userchoice == 3:
            scrape1.getlocation()
    else:
        print("That's not an option!")






# find the code in the body portion of the page and find a way to convert it all into text, while avoiding all the links that pop up, as well
# as random advertisements and such, fillers of the page to say
"""
URL = 'https://realpython.com/beautiful-soup-web-scraper-python/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id=True)
elements = results.find_all("div", class_="main-content")

# Send a GET request to the webpage
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all article titles
    article_titles = soup.find_all('h2', class_='entry-title')

    # Print the titles
    print(article_titles)
    for title in article_titles:
        print(title.text.strip())  # .strip() removes leading/trailing whitespaces
else:
    print("Failed to fetch webpage:", response.status_code)
"""
# URL of the webpage
"""
url = "https://realpython.com/beautiful-soup-web-scraper-python/"

# Fetch the HTML content of the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <div> elements with a specific class name
    div_elements = soup.find_all('div', class_='content')

    # Print the class names of the found div elements
    print(div_elements)
    for div in div_elements:
        print("Class name:", div['class'][0])
else:
    print("Failed to fetch webpage:", response.status_code)


for i in elements:
    pagetxt = i.find("p")
    print(pagetxt.text.strip())
    print()
"""

