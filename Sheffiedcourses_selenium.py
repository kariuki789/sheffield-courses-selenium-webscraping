from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv

chrome_driver_path = "/Users/user/Downloads/chromedriver-mac-x64/chromedriver"

# Set up Chrome options
options = Options()
options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

# Set up WebDriver
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

url = 'https://www.sheffield.ac.uk/undergraduate/courses/2023'
driver.get(url)

# Add a delay to wait for the page to load
time.sleep(2)

# Open CSV file and write header
with open('courses.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Course Name", "Award", "A Levels", "UCAS Code", "Duration", "Start Month", "Accreditation", "Home Students Fees", "Overseas Students Fees"])

    courses = driver.find_elements(By.CSS_SELECTOR, '.courselisting')
    total_records = 0
    complete_records = 0
    incomplete_records = 0
    for course in courses:
        course_name = course.find_element(By.CSS_SELECTOR, '.listcourse a').text
        course_link = course.find_element(By.CSS_SELECTOR, '.listcourse a').get_attribute('href')
        award = course.find_element(By.CSS_SELECTOR, '.listaward').text

        driver.get(course_link)

        # Add a delay to wait for the page to load
        time.sleep(2)

        total_records += 1
        all_found = True  # Assume all items will be found

        try:
            a_levels = driver.find_element(By.CSS_SELECTOR, '.ug-alevels-grades-text').text
        except:
            a_levels = 'Not found'
            all_found = False

        try:
            ucas_code = driver.find_element(By.CSS_SELECTOR, '.ug-ucas-code-text').text
        except:
            ucas_code = 'Not found'
            all_found = False

        try:
            duration = driver.find_element(By.CSS_SELECTOR, '.ug-course-length-text').text
        except:
            duration = 'Not found'
            all_found = False

        try:
            start_month = driver.find_element(By.CSS_SELECTOR, '.ug-start-month-feature').text
        except:
            start_month = 'Not found'
            all_found = False

        try:
            accreditation = driver.find_element(By.CSS_SELECTOR, '.ug-accredited-feature a').text
        except:
            accreditation = 'Not found'
            all_found = False

        try:
            home_students_fees = driver.find_element(By.CSS_SELECTOR, '.course-ug-fee-lookup .feebox:nth-child(1) .feecost').text
        except:
            home_students_fees = 'Not found'
            all_found = False

        try:
            overseas_students_fees = driver.find_element(By.CSS_SELECTOR, '.course-ug-fee-lookup .feebox:nth-child(2) .feecost').text
        except:
            overseas_students_fees = 'Not found'
            all_found = False

        # Write to CSV
        writer.writerow([course_name, award, a_levels, ucas_code, duration, start_month, accreditation, home_students_fees, overseas_students_fees])

        print(f'Course Name: {course_name}, Award: {award}, A Levels: {a_levels}, UCAS Code: {ucas_code}, Duration: {duration}, Start Month: {start_month}, Accreditation: {accreditation}, Home Students Fees: {home_students_fees}, Overseas Students Fees: {overseas_students_fees}')

        if all_found:
            complete_records += 1
        else:
            incomplete_records += 1

        # Go back to the list of courses
        driver.back()

        # Add a delay to wait for the page to load
        time.sleep(2)

    print(f"Total records: {total_records}")
    print(f"Complete records: {complete_records}")
    print(f"Incomplete records: {incomplete_records}")

driver.quit()
