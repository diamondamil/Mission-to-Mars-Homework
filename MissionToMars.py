# Import Dependencies\n",
    import os\n",
    import pandas as pd\n",
    from bs4 import BeautifulSoup as bs\n",
    from splinter import Browser\n",
    from selenium import webdriver\n",
    import selenium.webdriver.chrome.service as service\n",
    import requests\n",
    import time"

	
    #executable_path = {'executable_path': 'chromedriver.exe'},
    #browser = Browser('chrome', **executable_path, headless=False)
 
    #executable_path = {'executable_path': 'C:/Users/diamo/AppData/Local/pip/Cache/wheels/03/77/8b/811d5fc1d4a81d7aee893ce5cc585ec96f08955f049e523b32'}\n",
    #browser = Browser('chrome', **executable_path, headless= False)\n",
   

 ##"Mars News"##

   # Use requests and BeautifulSoup to scrape Nasa News for latest news\
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=mars&category=19%2C165%2C184%2C204&blank_scope=Latest'
    response = requests.get(url)
    soup = bs(response.text, 'lxml')


    #print news results
    
    news_title = results.find('div', class_='content_title').text
    newsp = results.find('div', class_='rollover_description').text
    print(news_title)
    print(newsp)


    ##"Mars Images"##

    #Enter mars images\n",
    url = 'https://jpl.nasa.gov/spaceimages/?search=&category=Mars\'
    browser.visit(url)

    #featured = mars_soup.find('div', class_='default floating_text_area ms-layer')\n",
    #featured_image = featured.find('footer')\n",
    #featured_image_url = 'https://www.jpl.nasa.gov'+ featured_image.find('a')['data-fancybox-href']\n",
    #print(str(featured_image_url))\n",
  
    #Code for moving through pages on site\n",
    time.sleep(5)\n",
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)\n",
    browser.click_link_by_partial_text('more info')
    time.sleep(5)\n",
   
    #Pull html text
    response = browser.html
   
    #Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response, 'html.parser')
  
    #Retrieve featured image\n",
    image_href = soup.find('figure', 'lede').a['href']
    link = 'https://www.jpl.nasa.gov'
    featured_image_url = link + image_href
    
    #Display
    print(featured_image_url)


    ##"Mars Weather Report"##

    #Get latest tweet for weather report
    twitter_url = 'https://twitter.com/marswxreport?lang=en'
    twitter_response = requests.get(twitter_url)
    twitter_soup = bs(twitter_response.text, 'lxml')
    twitter_result = twitter_soup.find('div', class_='js-tweet-text-container')
    
    #Retrieve latest tweet\n",
    mars_weather = twitter_result.find('p', class_='js-tweet-text').text
   
    #Display tweet
    print(mars_weather)

    ##"Mars Facts"##
    #Scrape Mars facts using PD fx
    mars_facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(mars_facts_url)

	
	
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
