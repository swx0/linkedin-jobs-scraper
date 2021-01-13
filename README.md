# Linkedin Jobs Scraper :mag:

## About
*Linkedin Jobs Scraper* extracts the following data from Linkedin search results:
- **Job data-id**

- **Location**

- **Company Name**

- **Position**

- **Job description**

Afterwhich, the data obtained would be written and saved in Google sheets using [Google Sheets API](https://developers.google.com/sheets/api) 
## Setup
To start scraping job information from Linkedin: 
1) Install these libraries: 
```
pip install selenium
pip install beautifulsoup4
pip install gspread
```
2) Find the respective [WebDriver](https://chromedriver.chromium.org/downloads) for your Chrome version. Save this chromedriver.exe in the same directory as the .py script 

3) Create [Google Cloud Platform](https://cloud.google.com/) account (if you haven't). Follow this [guide](https://gspread.readthedocs.io/en/latest/oauth2.html#) to authorize and authenticate access to the sheets. You should obtain the JSON file with credentials, rename this file as 'client_key.json' and save it in the same directory as the .py script. 
> :heavy_check_mark: Remember to share the created Google sheets with the client_email found in the JSON file.

4) Obtain a link from Linkedin that indicates your target position and location. The following is a sample link "https://www.linkedin.com/jobs/search/?keywords=Software%20Engineer&location=United%20States"

5) Read the comments in .py script, and edit:
    - String associated to the name of your Google Sheets
    - Link from step 4)

![demo](https://user-images.githubusercontent.com/76123658/104187049-449b1e00-5452-11eb-9bb4-b28860daeee8.gif)
