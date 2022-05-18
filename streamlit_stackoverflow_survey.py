# -*- coding: utf-8 -*-
"""
Created on Wed May 11 15:00:26 2022

@author: T430s
"""

# stack overflow survey analysis app
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import pickle 
with open('df_StackOverFlowSurvey', 'rb') as f: # rb = read the binary file
    df = pickle.load(f)
    


def count(x):
    return str(x).split(';')

df['languages'] = df['LanguageHaveWorkedWith'].apply(count) # no of language in from each responder
a = df['languages']

df_list=[] 
n = a.shape[0]   
for j in range(n):
    for i in a[j]: # each a[i] is a list and first need to extract it
        df_list.append(i)
    
df_list_language = pd.DataFrame(df_list) 
df_list_language = df_list_language[0].replace('nan',np.nan)
df_list_language = df_list_language.dropna()
languages = np.sort(df_list_language.unique()) 

# Header
st.header('Stack Overflow 2021 Survey--A.Maharjan')

# how many knew Python language already interms of # by each country? work on this, took me 2.5 hrs to figure it out for the first time
st.sidebar.header('Top Programming Languages')
lan = st.sidebar.selectbox('select the language',languages)

def count(x):
    return str(x).split(';')

def lang(x):
    language = lan
    if language in x: # note that x is a list as a data frame element
        return(1)
    else:
        return(0)

df['languages'] = df['LanguageHaveWorkedWith'].apply(count) 
df['Python'] = df['languages'].apply(lang)   
lan_plot = df.groupby('Country')['Python'].sum().sort_values(ascending = False)[:20] # total users of Python by country     

if st.sidebar.button('Top Languages'):
    st.set_option('deprecation.showPyplotGlobalUse', False) # not to print the error message
    lan_plot.plot(kind='bar')
    plt.title('Most popular languages/ Top 2o countries')
    plt.show()
    st.pyplot()


# search the country by initial name
text_input = st.sidebar.text_input('Enter Country Initial/Intial Letter Capital',"")
if st.sidebar.button("Searh Country"):
    bool_series = df['Country'].str.startswith(text_input)
    name = df[bool_series]['Country'].unique()
    st.write(name)





# popular languages by country
st.sidebar.header('Choose the Country')
con = df['Country'].unique()
con = np.sort(con) # as con becomes a numpy array
country = st.sidebar.selectbox('select the country',con)

df_country = df[df['Country'] == country]  
df_country['languages'] = df_country['LanguageHaveWorkedWith'].apply(count)
b = df_country['languages'].reset_index() # it filters some random index based on the country positions, so has to do rest index first
b = b.iloc[:,1] # removing the old random indexing

df_list_c=[] 
n = b.shape[0]   
for j in range(n):
    for i in b[j]: # each a[i] is a list and first need to extract it
        df_list_c.append(i)
    
df_list_language_c = pd.DataFrame(df_list_c)    

if st.sidebar.button('Top Languages by Country'):
    st.set_option('deprecation.showPyplotGlobalUse', False) # not to print the error message
    df_list_language_c[0].value_counts().plot(kind='bar')
    plt.title(country)
    plt.ylabel('Top Programming languages')
    plt.show()
    st.pyplot()

# education level by country
ed_plot = df.groupby('Country')['EdLevel'].value_counts()[country] # value counts automatically ignnores the nans 
if st.sidebar.button('Education Level by Country'):
    st.set_option('deprecation.showPyplotGlobalUse', False) # not to print the error message
    ed_plot.plot(kind='bar')
    plt.title(country)
    plt.ylabel('Education label Users')
    plt.show()
    st.pyplot()




# data base already using by country
df_db = df[df['Country'] == country]
df_db['database'] = df_country['DatabaseHaveWorkedWith'].apply(count)
a = df_db['database'].reset_index() # it filters some random index based on the country positions, so has to do rest index first
a = a.iloc[:,1] # removing the old random indexing

df_list=[] 
n = a.shape[0]   
for j in range(n):
    for i in a[j]: # each a[i] is a list and first need to extract it
        df_list.append(i)
    
df_list_database = pd.DataFrame(df_list)    

df_db_plot = df_list_database[0].value_counts().plot(kind='bar')  
 
if st.sidebar.button('DataBase software use by Country'):
    st.set_option('deprecation.showPyplotGlobalUse', False) # not to print the error message
    df_db_plot
    plt.title(country)
    plt.ylabel('DataBase Users')
    plt.show()
    st.pyplot()





# overall summary
st.sidebar.header('Overall Summary')
   
# salary by country
if st.sidebar.button('Annual Salary by Country'):
    
    df.groupby('Country')['ConvertedCompYearly'].agg(['mean','median']).sort_values(by='median',ascending=False)[0:100]
    


       
# by gender
if st.sidebar.button('Users by Gender'):
    
    df.Gender.value_counts()[0:5].plot(kind='bar')
    plt.title('Users by Gender')
    plt.show()
    st.pyplot()
    



# by ethnicity
if st.sidebar.button('Users by Ethnicity'):
    
    df.Ethnicity.value_counts()[0:10].plot(kind='bar')
    plt.title('Users by Ethnicity')
    plt.show()
    st.pyplot()





# where did you get help/support?
#df.NEWStuck[0]
a = df['NEWStuck'].apply(count) # each element is a list

df_list=[] 
n = a.shape[0]   
for j in range(n):
    for i in a[j]: # each a[i] is a list and first need to extract it
        df_list.append(i)
    
df_list_help = pd.DataFrame(df_list)    

if st.sidebar.button('Help From ?'):
    st.set_option('deprecation.showPyplotGlobalUse', False)
    df_list_help[0].value_counts().plot(kind='bar')
    plt.title('Help/Support Source')
    plt.show()
    st.pyplot()



# learn code from?
learn_coding = df.LearnCode.value_counts().sort_values(ascending=False)[0:20]
if st.sidebar.button('Learn Code From ?'):
    st.write(learn_coding)
    
    
    
if st.sidebar.button('Current Profession'):
    
    df.MainBranch.value_counts().plot(kind='bar')
    plt.title('Profession')
    plt.show()
    st.pyplot()



# waveframe knowledge
a = df['WebframeHaveWorkedWith'].apply(count) # each element is a list

df_list=[] 
n = a.shape[0]   
for j in range(n):
    for i in a[j]: # each a[i] is a list and first need to extract it
        df_list.append(i)
    
df_list_Webframe = pd.DataFrame(df_list)    
df_list_Webframe[0].value_counts() # value counts is a series method, applying it on [0]
# plot
if st.sidebar.button('WebFramework'):
    
    df_list_Webframe[0].value_counts().plot(kind='bar')
    plt.title('WebFramework')
    plt.show()
    st.pyplot()









