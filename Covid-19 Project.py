#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Data collected from "https://covid19.who.int/WHO-COVID-19-global-data.csv"
# pip install matplot
# pip install pandas
# pip install numpy


# In[ ]:


import os
import urllib
import matplotlib.pyplot as Mat
import pandas as pd
import numpy as np


# In[ ]:


url = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
file_path = os.path.join("data","covid")


# In[ ]:


os.makedirs(file_path, exist_ok=True)
csv_path = os.path.join(file_path,"WHO-COVID-19-Data.csv")
urllib.request.urlretrieve(url, csv_path)


# In[ ]:


DataF = pd.read_csv(csv_path)


# In[ ]:


DataF


# In[ ]:


DataF_index = DataF.index
DataF_index


# In[ ]:


DataF_columns = DataF.columns
DataF_columns


# In[ ]:


DataF_index.values


# In[ ]:


DataF.values


# In[ ]:


DataF.dtypes


# In[ ]:


DataF.shape


# In[ ]:


DataF.head()


# In[ ]:


DataF.tail()


# In[ ]:


DataF.info()


# In[ ]:


DataF.describe()


# In[ ]:


DataF["Country"]


# In[ ]:


DataF["Country"].unique()


# In[ ]:


DataF["Country_code"].unique()


# In[ ]:


DataF.columns = [col.strip() for col in DataF.columns]
DataF.columns


# In[ ]:


DataF.Country


# In[ ]:


DataF.loc[1:4, "Country"]


# In[ ]:


DataF.loc[1:8,["Country", "New_cases"]]


# In[ ]:


DataF.Country == "India"


# In[ ]:


DataF[DataF.Country == "India"]


# In[ ]:


DataF[DataF.New_deaths > 1000]


# In[ ]:


DataF.loc[(DataF.New_deaths > 1000) & (DataF.Country_code=="IN"),["Date_reported","Country_code","Country","New_deaths","New_cases"]]


# In[ ]:


DataF.loc[DataF.Country_code == "IN",["New_cases"]].max()


# In[ ]:


DataF.loc[DataF.Country_code == "IN",["New_deaths"]].max()


# In[ ]:


DataF.loc[DataF.Country_code == "IN",["New_deaths"]].sum()


# In[ ]:


#DataC = pd.read_csv("c:\\Users\\yurik\\data\\covid\\WHO-COVID-19-Data.csv")


# In[ ]:


#DataC = pd.DataFrame(DataC)


# In[ ]:


# Ploting Data 
#DataCountry = DataC["Country"]
#DataNCases = DataC["New_cases"]
#DataCCases = DataC["Cumulative_cases"]
#DataNDeaths = DataC["New_deaths"]
#DataCDeaths = DataC["Cumulative_deaths"]

