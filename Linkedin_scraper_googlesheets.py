from selenium import webdriver
from bs4 import BeautifulSoup
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/spreadsheets'
    ]
file_name = 'client_key.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)

# Open the designated sheet
sheet = client.open('job description').sheet1 # rename the string according to the name of your google sheets

current_row = 2

driver = webdriver.Chrome()


def data_id(IDsoup):
    return [item['data-id'] for item in IDsoup.find_all('li', attrs={'data-id' : True})] 


# Job search - position, location (edit link accordingly)
driver.get('https://www.linkedin.com/jobs/search/?keywords=Software%20Engineer&location=United%20States') 
time.sleep(1)

# Infinte scrolling
while True:
    
    # Scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    count = 0 
    while count < 25:
        
        # Wait for page to load
        time.sleep(2)
        
        # Expand job description of selected job (Show More button)
        driver.find_element_by_css_selector("[aria-label='Show more']").click()
        
        
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        # print(soup.prettify())
        
        # data-id of selected job (active job card)
        IDhtml = soup.find_all('li', class_='result-card job-result-card result-card--with-hover-state job-card__contents--active')
        IDsoup = BeautifulSoup(str(IDhtml[0]), 'html.parser')
        print(data_id(IDsoup))
        print()
        
        dataID = data_id(IDsoup)[0]
        sheet.update_cell(current_row,1,dataID) # data-id in 1st column  
        
        # Update Company name, Location and Position on Google Sheets
        company = soup.find_all('span', class_='topcard__flavor')
        company = company[0].find_all('a', class_='topcard__org-name-link topcard__flavor--black-link')
        print(company[0].text)
        print()
        
        company_string = company[0].text
        sheet.update_cell(current_row,2,company_string) # Company name in 2nd column


        position = soup.find_all('h2', class_='topcard__title')
        print(position[0].text)
        print()

        position_string = position[0].text
        sheet.update_cell(current_row,3,position_string) # Position in 3rd column 
        
           
        location = soup.find_all('span', class_='topcard__flavor topcard__flavor--bullet')
        print(location[0].text)
        print()

        location_string = location[0].text
        sheet.update_cell(current_row,4,location_string) # Location in 4th column  
        
        # Wait for page to load
        time.sleep(1)
        
        # Update Job Description (bullet points only)
        descList = soup.find_all('div', class_='show-more-less-html__markup') 
        bulletpointList = descList[0].find_all('li')
        bulletpoint_fullstring = ''
        for bulletpoint in bulletpointList:
            bulletpoint_fullstring += str(bulletpoint.text) + '\n'
        sheet.update_cell(current_row,5,bulletpoint_fullstring) # Job Description in 5th column 
        print(bulletpoint_fullstring)
        print()
                
        # Click on the next job card
        current_job = soup.find('li','result-card job-result-card result-card--with-hover-state job-card__contents--active')
        next_job = current_job.find_next_sibling('li')
        IDsoup = BeautifulSoup(str(next_job), 'html.parser')
        next_job_id = data_id(IDsoup)[0]
        driver.find_element_by_css_selector("[data-id='{}']".format(next_job_id)).click()
        
        current_row += 1
        count += 1
        
    # Scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Wait for page to load
    time.sleep(1)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
