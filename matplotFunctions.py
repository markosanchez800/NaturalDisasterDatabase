import matplotlib.pyplot as mpl
import streamlit as st
import pandas as pd
import numpy as np

def barChart(df,x,y):
    #CURRENTLY ONLY WORKS FOR TOTAL OCCURENCES AND TOTAL DEATHS FOR X
    height = 600
    if y == 'Total Disasters':
        counts = df[x].value_counts().sort_values(ascending=True)
        fig, ax = mpl.subplots(figsize=(8,max(4,len(counts)*0.3)))
        ax.barh(counts.index,counts.values,color='forestgreen',edgecolor='black')
    else:
        quals = sorted(df[x].dropna().unique())
        quants = df.groupby(x)[y].sum().reset_index()
        st.write(quants)
        quantTuple = tuple(quants[y])
        fig, ax = mpl.subplots(figsize=(8,max(4,len(quals)*0.3)))
        ax.barh(quals,quantTuple,color='forestgreen',edgecolor='black')
    ax.set_xlabel(f'{x}')
    ax.set_ylabel(f'{y}')
    ax.margins(y=0.005)
    fig.tight_layout()
    st.title(f'{y} by {x}')
    with st.container(height=height):
        st.pyplot(fig)

def lineGraph():
    return(1)

def pieChart(df,x,y):
    #CURRENTLY ONLY WORKS FOR TOTAL OCCURENCES OF X AND MOST CHARTS ARE TOO PACKED FOR READABILITY
    #MAYBE ONLY PLOT TOP 5-6 FOR PIE CHART?
    counts = df[x].value_counts()
    fig, ax = mpl.subplots()
    ax.pie(counts.values,labels=counts.index,autopct='%1.1f%%', shadow=True,startangle=90)
    ax.axis('equal')
    st.title(f'{y} by {x}')
    st.pyplot(fig)
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


