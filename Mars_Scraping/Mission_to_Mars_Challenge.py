#!/usr/bin/env python
# coding: utf-8

# In[329]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 


# In[330]:


#Create an instance of a Splinter browser 
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[331]:


# Visit the mars nasa news site
url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
browser.visit(url)
# Optional delay for loading the page before searching for the tag/attribute element 
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[332]:


# Set up the HTML parser 
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[333]:


# Find the content titles out of the variable assigned above 
slide_elem.find('div', class_='content_title')


# In[334]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[335]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[336]:


# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# In[337]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[338]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[339]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[340]:


# Use the base URL to create an absolute URL
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


# In[341]:


# Read the HTML from the scraped table into a Pandas DataFrame 
df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[342]:


# Convert the DataFrame back to HTML-ready code
df.to_html()


# ## D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# #### Hemispheres

# In[343]:


# 1. Use browser to visit the URL 
url = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/index.html'
browser.visit(url)

# Optional delay for loading the page before searching for the tag/attribute element 
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[344]:


# 2. Create a list of dictionaries to hold the images and titles.
hemisphere_image_urls = []
# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Find and click the full image button

for x in range(0,4):
    browser.is_element_present_by_css('div.list_text', wait_time=2)
    results = browser.find_by_css('a.product-item img', wait_time=2)
    result = results[x]
    result.click()
    browser.is_element_present_by_css('div.list_text', wait_time=2)
    html = browser.html
    mars_soup = soup(html, 'html.parser')
    img_url_var = mars_soup.find(string = 'Sample').find_parent('a').get('href')
    img_full_url = f'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/{img_url_var}'
    title_var = mars_soup.find('div', class_='cover').find('h2', class_='title').text
    hemisphere_image_urls.append({'image url':img_full_url, 'title': title_var})
    
    browser.back()


# In[345]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[346]:


# 5. Quit the browser
browser.quit()


# In[ ]:




