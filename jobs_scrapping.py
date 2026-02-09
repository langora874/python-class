from bs4 import BeautifulSoup
import requests
url="https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Python%2C&cboWorkExp1=-1&txtLocation="
html_file=requests.get(url).text
#print(html_file)
soup=BeautifulSoup(html_file,'html.parser')

jobs = soup.find_all('div', class_="srp-listing clearfix")
for job in jobs:
    title=job.find('h3').text.strip()
    experience=job.find('div',class_="srp-exp").text.strip()
    print(f"Job title: {title}")
    print(f"Job  experience: {experience}\n")