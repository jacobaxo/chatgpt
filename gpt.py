import csv
import requests
from bs4 import BeautifulSoup

# Make a request to the weather.com website to get the HTML of the webpage
url = "https://weather.com/weather/tenday/l/USNY0996:1:US"
response = requests.get(url)

# Use BeautifulSoup to parse the HTML of the webpage
soup = BeautifulSoup(response.text, "html.parser")

# Extract the relevant data from the webpage
data = []
forecast_items = soup.find_all(class_="twc-table")
for forecast in forecast_items:
    date = forecast.find(class_="date-time").get_text()
    description = forecast.find(class_="description").get_text()
    temp = forecast.find(class_="temp").get_text()
    data.append((date, description, temp))

# Write the data to a CSV file
with open (f"forecast.csv", "w", newline="{forecast_items}") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)