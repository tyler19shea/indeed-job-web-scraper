# indeed-job-web-scraper
This project is a web scraper that extracts job listings from Indeed.com based on a specified job title and location. It utilizes Selenium for browsing and BeautifulSoup for parsing HTML content. The scraped data is saved into a CSV file for further analysis.
# Prerequisites
- Python 3.x
- 'selenium' library
- 'beautifulsoup4' library
- 'pandas' library
- Chrome browser
- ChromeDriver
# Setup
Install Required Python Libraries using 'pip':
```
pip install selenium beautifulsoup4 pandas
```
Download ChromeDriver
- Check your Chrome browser version by navigating to chrome://settings/help.
- Download the corresponding version of ChromeDriver.
- Extract the downloaded file and place the chromedriver executable in your project directory.
# Usage
- Clone this repository or copy the provided code into a new Python script file.
- Run the script:```python indeed_scraper.py```
- You will be prompted to enter the job title and location.
```
Job Role to search for: Data Scientist
Identify location to look for (remote): San Francisco, CA
```
- The script will scrape job listings from Indeed.com based on the provided criteria and save the data into a CSV file named 'indeed_jobs.csv'
# Script Detials
Functions:
- 'create_driver()': Initializes the Selenium WebDriver with a minimal window configuration.
- 'fetch_web_page(driver, url)': Loads the specified URL using Selenium and returns the page source.
- 'parse_html(content)': Parses the HTML content using BeautifulSoup and extracts job cards.
- 'extract_job_data(job_cards)': Extracts job details such as title, company, location, summary, and job link from each job card.
- 'get_next_page(soup)': Identifies the URL for the next page of job listings and returns it.
- 'save_to_csv(job_list, filename='indeed_jobs.csv')': Saves the extracted job data into a CSV file.
# Main Flow
- Initialize the WebDriver
- Fetch the first page of job listings
- Parse the HTML content and extract job data
- Check for the next page and repeat 2-4 until no more pages are found.
- Save the collected job data into a CSV file.
- Quit the WebDriver
# Example Output
```
Job Role to search for: Data Scientist
Identify location to look for (remote): San Francisco, CA
Fetching next page
Fetching next page
No more pages
Data saved to indeed_jobs.csv
```
The script will create a file 'indeed_jobs.csv' containing the scraped job listings with the following columns: Title, Company, Location, Summary, and Link
# Troubleshooting
- Ensure that the 'chromedriver' version matches your Chrome browser version
- If the script fails to initialize the WebDriver, verify the path to 'chromedriver' and ensure it has execute permissions
- If the script encounters an error during execution, the error message will be printed to the console. Check the message for clues on what went wrong