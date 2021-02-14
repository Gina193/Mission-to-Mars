#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install webdriver_manager


# In[2]:


import pandas as pd 
import numpy as np


# In[3]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup


# In[4]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path)


# In[5]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[6]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[7]:


slide_elem.find("div", class_='content_title')


# In[8]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[9]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# In[10]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[11]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[12]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[13]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[14]:


# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[15]:


# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# In[16]:


df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# In[17]:


df.to_html()


# In[18]:


browser.quit()


# In[19]:


# # Import Splinter, BeautifulSoup, and Pandas
# from splinter import Browser
# from bs4 import BeautifulSoup as soup
# import pandas as pd


# In[20]:


#pip install webdriver_manager


# In[21]:


# Path to chromedriver
get_ipython().system('which chromedriver')
#C:\Users\SoutexEng2\OneDrive\Desktop\MJ\Mattie_DATA_Visualization\DATA Projects\MarsMod10\Mission-to-Mars


# In[23]:


# # Set the executable path and initialize the chrome browser in splinter
# executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
# #executable_path = {'executable_path': 'C:\Users\SoutexEng2\OneDrive\Desktop\MJ\Mattie_DATA_Visualization\DATA Projects\MarsMod10\Mission-to-Mars'}
# browser = Browser('chrome', **executable_path)

executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path)


# ### Visit the NASA Mars News Site

# In[24]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')

slide_elem.find("div", class_='content_title')


# In[25]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### JPL Space Images Featured Image

# In[26]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[27]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[28]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[29]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[32]:


# find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[33]:


# find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel

# Use the base url to create an absolute url
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# ### Mars Facts

# In[34]:


df = pd.read_html('http://space-facts.com/mars/')[0]

df.head()

df.columns=['Description', 'Value']
df.set_index('Description', inplace=True)
df

#df.to_html()


# In[35]:


df.to_html()


# ### Mars Weather

# In[36]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)

# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')

# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())

# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles


# ### Hemispheres

# In[37]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[38]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
image_urls = []
titles = []


# In[39]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
#html = browser.html
browser.find_by_css("a.product-item")
links = browser.find_by_css("a.product-item h3")

for i in range(len(links)):
    hemisphere = {}
    browser.find_by_css("a.product-item h3")[i].click()
    browser.links.find_by_text("Sample").first
    image_link = browser.links.find_by_text("Sample").first["href"]
    
    browser.find_by_css("h2.title").text
    title = browser.find_by_css("h2.title").text
    print(image_link)
    print(title)
    hemisphere_image_urls.append({"Title": title, "Image_link": image_link})
    browser.back()


#hemisphere_image_urls.image
#mars_hemisphere_soup = 
#product_list = mars_hemispheres


# In[40]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[41]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]: