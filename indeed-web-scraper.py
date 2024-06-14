import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def fetch_web_page (url):
    driver.get(url)
    time.sleep(3)
    return driver.page_source

def parse_html(content):
    soup = BeautifulSoup(content, "html.parser")
    job_cards = soup.find_all('div', class_='slider_container')
    return job_cards

def extract_job_data(job_cards):
    job_list = []

    for item in job_cards:
        title = item.find('h2', class_='jobTitle').text
        company = item.find('span', class_='css-63koeb').get_text()
        location = item.find('div', class_='css-1p0sjhy').get_text()
        summary = item.find('div', class_='css-9446fg').get_text()
        job_list.append({'Title': title, 'Company': company, 'Location': location, 'Summary': summary})
    return job_list

def save_to_csv(job_list, filename='indeed_jobs.csv'):
    df = pd.DataFrame(job_list)
    df.to_csv(filename, index=False)
    print(f'Data saved to {filename}')

def main():
    url = f"https://www.indeed.com/jobs?q={job_title}&l={location}"

    content = fetch_web_page(url)
    job_cards = parse_html(content)
    jobs = extract_job_data(job_cards)

    save_to_csv(jobs)


if __name__ == '__main__':
    job_title = input("Job Role to search for: ")
    location = input("Identify location to look for (remote): ")
    try:
        driver = webdriver.Chrome()
        main()
    except Exception as e:
        print(f'Error: {e}')
    finally:
        driver.quit()





