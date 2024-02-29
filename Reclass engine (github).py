#!/usr/bin/env python
# coding: utf-8

# This reclassification engine is a powerful tool to classify transactions into their actual categories. I have stress tested this for over a million lines, without exception. Before you start processing this file, please ensure you have Pandas (pip install pandas), Datetime (pip install datetime) & Numpy (pip install numpy) libraries installed:
# 
# Please ensure you exactly specify field/column names that you select for reclassifying in code line 5 .
# 
# Please specify input and output file paths (in CSV format) in code lines 3 & 4. Output file does not need to exist and will be created and opened automatically once code executes.

# In[ ]:


#Import required libraries
import os
import pandas as pd
import numpy as np
from datetime import *


# In[ ]:

st.sidebar.image('st_logo.png')
st.sidebar.write("👋 Hi, I’m Shishir! I've always loved tinkering with things.")
st.sidebar.write("🌱 I’m a Data Scientist at Intel. I am also a Masters in Data Science Student at Northwestern.")
st.sidebar.write("📫 Reach me @ shishir.rd@gmail.com")
st.sidebar.write("My Github is https://github.com/shishirrd")


current_date_and_time = datetime.now()
current_date_and_time = current_date_and_time.strftime("%Y-%m-%d %H:%M:%S")
current_date_and_time = str(current_date_and_time).replace(":","-")
current_date_and_time_string = str(current_date_and_time)
extension = ".csv"


# In[ ]:


#Please specify csv filepaths prior to every run
input_file = 


# In[ ]:


base=os.path.basename(input_file)
input_path = os.path.splitext(base)[0]+" "


# In[ ]:


#Auto derived based on input file name and filepath
output_file = input_path + (current_date_and_time_string) + extension


# In[ ]:


#Specify fields for reclassification
field1 = 'Entry Description'
field2 = 'Supplier Name'
field3 = 'PO description'


# In[ ]:


#Read input file
df = pd.read_csv(input_file) 


# In[ ]:


#Convert field 1 to lowercase
df[field1] = df[field1].str.lower()


# In[ ]:


#Convert field 2 to lowercase
df[field2] = df[field2].str.lower()


# In[ ]:


#Convert field 3 to lowercase
df[field3] = df[field3].str.lower()


# In[ ]:


#Replace blanks with "0" to avoid erroneous tagging
df = df[[field1, field2, field3]].replace(np.nan, "0")


# In[ ]:


#Create classifier column with a default value
df['category'] = "Not Classified"


# In[ ]:


#Phone bills and other communication expense test
df['category'] = np.where(df[field1].str.contains('phone bill|internet|postage|stamp'), 'Communication', df['category'])


# In[ ]:


#Power, fuel & water test
df['category'] = np.where(df[field1].str.contains('ac charge|generator|diesel|electric|water'), 'Power, Fuel & Water', df['category'])


# In[ ]:


#Repairs & Maintenance vendor test
df['category'] = np.where(df[field2].str.contains('supplier1|supplier2|supplier3'), 'Repairs & Maintenance', df['category'])


# In[ ]:


#Travel expense vendor test
df['category'] = np.where(df[field2].str.contains('supplier1|supplier2|supplier3'), 'Travel', df['category'])


# In[ ]:


#Professional expense vendor test
df['category'] = np.where(df[field2].str.contains('supplier1|supplier2|supplier3'), 'Professional', df['category'])


# In[ ]:


#Facility vendor test
df['category'] = np.where(df[field2].str.contains('supplier1|supplier2|supplier3'), 'Facility', df['category'])


# In[ ]:


#Rent vendor test
df['category'] = np.where(df[field2].str.contains('supplier1|supplier2|supplier3'),'Rent Expense', df['category'])


# In[ ]:


#Outsourcing expense test
df['category'] = np.where(df[field3].str.contains('outsourc|contingent|temporary'), 'Outsourcing expense', df['category'])


# In[ ]:


#Prepaid maintenance test
df['category'] = np.where(df[field3].str.contains('1 y|2 y|3 y|4 y|maint|support|exten|warranty'), 'Prepaid Maintenance', df['category'])


# In[ ]:


#Open CSV file in EXCEL
#Local path in dir
from pathlib import Path
absolutePath = Path(output_file).resolve()
os.system(f'start excel.exe "{absolutePath}"')

