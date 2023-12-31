# Sheffield  courses web scraping
The code uses the Selenium library to scrape data from the University of Sheffield's website about undergraduate courses offered in 2023. The data that is scraped includes the course name, award, A Levels, UCAS code, duration, start month, accreditation, home students fees, and overseas students fees. The data is then written to a CSV file.

The code first sets up the Chrome driver and opens the Sheffield University website. It then uses the find_elements() method to find all of the course listings on the page. For each course listing, the code gets the course name, award, and a link to the course's individual page. The code then clicks on the link to the course's individual page and scrapes the following data:

A Levels
UCAS code
Duration
Start month
Accreditation
Home students fees
Overseas students fees
The data is then written to the CSV file. The code repeats this process for all of the course listings on the page. Once all of the data has been scraped, the code prints the total number of records, the number of complete records, and the number of incomplete records. The code then quits the Chrome driver.

Here are some of the key features of the code:

It uses the Selenium library to scrape data from a website.
It writes the data to a CSV file.
It tracks the number of complete and incomplete records.
