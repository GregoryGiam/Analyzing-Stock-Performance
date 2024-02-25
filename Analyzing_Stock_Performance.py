#!/usr/bin/env python
# coding: utf-8

# <h1>Extracting Stock Data Using a Python Library</h1>
# 

# <p>You are a data scientist working for a hedge fund; it's your job to determine any suspicious stock activity. In this lab you will extract stock data using a Python library. We will use the <coode>yfinance</code> library, it allows us to extract data for stocks returning data in a pandas dataframe. </p>
# 

# <h2>Table of Contents</h2>
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <ul>
#         <li>Using yfinance to Extract Stock Info (Workaround provided as current yf .info method does not work)</li>
#         <li>Using yfinance to Extract Historical Share Price Data</li>
#         <li>Using yfinance to Extract Historical Dividends Data</li>
#     </ul>
# Now we can access functions and variables to extract the type of data we need. You can view them and what they represent here https://aroussi.com/post/python-yahoo-finance.
# 
# 
# <hr>
# 

# In[1]:


get_ipython().system('pip install yfinance==0.2.4')
#!pip install pandas==1.3.3


# In[2]:


import yfinance as yf
import pandas as pd


# Using the `Ticker` module we can create an object that will allow us to access functions to extract data. To do this we need to provide the ticker symbol for the stock, here the company is Apple and the ticker symbol is `AAPL`.
# 

# In[3]:


apple = yf.Ticker("AAPL")


# ### Stock Info
# Using yf <code>info</code> method should have been able to provide information about the stock as a Python dictionary.
# 
# Using the workaround, as current yf .info method does not work.
# 
# This code snippet below effectively downloads the content of the specified URL and saves it to a local file named "apple.json."
# 

# In[4]:


# Use the requests library to send an HTTP GET request to the specified URL (url).
# Store response in the response variable.

import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"
response = requests.get(url)

# Open a local file named "apple.json" in binary write mode ("wb") and write the binary content of the HTTP response (response.content) to the local file.

with open("apple.json", "wb") as file:
    file.write(response.content)


# In[5]:


# Use the json module to open the local file "apple.json" and load its content as a Python object (apple_info).
# The content of "apple.json" is assumed to be in JSON format.

import json
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
apple_info


# We can get the <code>'country'</code> using the key country
# 

# In[6]:


apple_info['country']


# ### Extracting Share Price
# 

# A share is the single smallest part of a company's stock  that you can buy, the prices of these shares fluctuate over time. Using the <code>history()</code> method we can get the share price of the stock over a certain period of time. Using the `period` parameter we can set how far back from the present to get data. The options for `period` are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.
# 

# In[7]:


apple_share_price_data = apple.history(period="max")


# The format that the data is returned in is a Pandas DataFrame. With the `Date` as the index the share `Open`, `High`, `Low`, `Close`, `Volume`, and `Stock Splits` are given for each day.
# 

# In[8]:


apple_share_price_data.head()


# We can reset the index of the DataFrame with the `reset_index` function. We also set the `inplace` paramter to `True` so the change takes place to the DataFrame itself.
# 

# In[9]:


apple_share_price_data.reset_index(inplace=True)


# We can plot the `Open` price against the `Date`:
# 

# In[10]:


apple_share_price_data.plot(x="Date", y="Open")


# ### Extracting Dividends
# 

# Dividends are the distribution of a companys profits to shareholders. In this case they are defined as an amount of money returned per share an investor owns. Using the variable `dividends` we can get a dataframe of the data. The period of the data is given by the period defined in the 'history` function.
# 

# In[11]:


apple.dividends


# We can plot the dividends overtime:
# 

# In[12]:


apple.dividends.plot()


# ## Another example 
# 

# Now using the `Ticker` module create an object for AMD (Advanced Micro Devices) with the ticker symbol is `AMD` called; name the object <code>amd</code>.
# 
# Similar method as above code for Apple is used for AMD below.

# In[13]:


import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json"
response = requests.get(url)

with open("amd.json", "wb") as file:
    file.write(response.content)


# In[14]:


import json
with open('amd.json') as json_file:
    amd_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
amd_info


# Obtain stock data for AMD using the `history` function and finding the `Volume` traded on the first day (first row).
# 

# In[16]:


amd = yf.Ticker("AMD")
amd_share_price = amd.history(period='max')
amd_share_price.head(1)['Volume']


# In[ ]:




