import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime

### Variables for setup
URL = "Your WillyWeather URL"
token = "Your Pushover Token"
user = "Your Pushover User"
first_name = "Your Firstname"

### Scrape Data

# Set up headless Chrome browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

# Define web driver
driver = webdriver.Chrome(options=chrome_options)

# Open forecast page
driver.get(URL)

# Parse HTML
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Locate today's max element
findTemp = soup.find("li", class_="day").find("li", class_="max")

# Variable for convenience (w/ appended units)
maxTemp = f"{findTemp.contents[0]}°C"

# Open rain subdomain
driver.get(URL.replace("www", "rainfall"))

# Parse HTML
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Locate today's chance of rain
findChance = soup.find("li", class_="day").find("b", class_="chance-value")

# Variable for convenience
rainChance = findChance.contents[0]

# Locate today's rain amount
findRain = soup.find("li", class_="day").find("b", class_="chance-amount")

# Variable for convenience
rainAmount = findRain.contents[0]

# Terminate headless browser instance
driver.quit()

### Send data via notification

output = f"Good morning, {first_name}. Max temp is {maxTemp}, with {rainChance} chance of rain ({rainAmount} expected). Have a nice day."

pushover_params = {
    "token": token,
    "user": user,
    "message": output
}

post_output = requests.post("https://api.pushover.net/1/messages.json", params=pushover_params)