# Linkedin Jobs Scraper

## About
*Linkedin Jobs Scraper* extracts the following data from Linkedin search results:
- **Job data-id**

- **Location**

- **Company Name**

- **Position**

- **Job description**

Afterwhich, the data obtained would be written and saved in Google sheets using Google Sheets API 
## Setup
To start scraping job information from Linkedin: 
1) Obtain a link from Linkedin that indicates your target position and location. The following is a sample link "https://www.linkedin.com/jobs/search/?keywords=Software%20Engineer&location=United%20States"

2) Install these libraries: 
```
pip3 install selenium
pip3 install beautifulsoup4
pip3 install gspread
```
3) Find the respective [WebDriver](https://chromedriver.chromium.org/downloads) to your Chrome version. Save this chromedriver.exe in the same directory as the .py script 

4) Create [Google Cloud Platform](https://cloud.google.com/) account (if you haven't). Follow this [guide](https://gspread.readthedocs.io/en/latest/oauth2.html#) to authorize and authenticate access to the sheets. You should obtain the JSON file with credentials, rename this file as 'client_key.json' and save this file in the same directory as the .py script. 

