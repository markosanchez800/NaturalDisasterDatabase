import matplotlib.pyplot as mpl
import streamlit as st
import pandas as pd

def barChart(x,y):
    #dbarChart = mpl.bar(x,y,color='forestgreen',edgecolor='lemonchiffon',width=0.6)
    fig,ax = mpl.subplots()
    ax.plot(x,y,color='forestgreen')
    st.pyplot(fig)

def lineGraph():
    return(1)

#Pre-Made Charts

def disastersByContinent(df):
    #Pie chart
    counts = df['Continent'].value_counts()
    fig, ax = mpl.subplots()
    ax.pie(counts.values,labels=counts.index,autopct='%1.1f%%', shadow=True,startangle=90)
    ax.axis('equal')
    st.title('Disasters by Continent')
    st.pyplot(fig)

def disastersByCountry(df):
    height = 600
    counts = df['Country'].value_counts().sort_values(ascending=True)
    fig, ax = mpl.subplots(figsize=(8,max(4,len(counts)*0.3)))
    ax.barh(counts.index,counts.values,color='forestgreen',edgecolor='black')
    ax.set_xlabel('Total Disasters')
    ax.set_ylabel('Country')
    ax.margins(y=0.005)
    fig.tight_layout()
    st.title('Disasters by Country')
    with st.container(height=height):
        st.pyplot(fig)

def disastersByYear(df):
    height = 600
    counts = df['Year'].value_counts().sort_values(ascending=True)
    fig, ax = mpl.subplots(figsize=(8,max(4,len(counts)*0.3)))
    ax.barh(counts.index,counts.values,color='forestgreen',edgecolor='black')
    ax.set_xlabel('Total Disasters')
    ax.set_ylabel('Year')
    ax.margins(y=0.005)
    fig.tight_layout()
    st.title('Disasters by Year')
    with st.container(height=height):
        st.write('Keep in mind, data collection has increased over the years and this influences total amounts')
        st.pyplot(fig)

#Types of possible charts:
#Disasters by year
#Disasters by location
#Types of disasters in locations
#Fatalities by disaster type


