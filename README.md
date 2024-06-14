# indeed-job-web-scraper
This program utilizes the selenium library to scrape through a dynamic website. The website it scrapes is indeed and then places its contents into a csv file to organize it. 

The libraries used are the BeautifulSoup library to handle the HTML content and then pandas library (along with the selenium library). The libraries can be installed by utilizing the folowing command:
pip install pandas selenium beautifulsoup4

The program fetches the web page using the chrome webdriver and returns the contents of the of page to be parsed using the BeautifulSoup library. The parsed data is then saved into a csv after placing the data into a pandas Data Frame. 

I would like to add a more dynamic approach where the I can input the job title and location to search for. Another addition that would be benificial would be the ability to to get the other pages of the website so the list can be longer. 