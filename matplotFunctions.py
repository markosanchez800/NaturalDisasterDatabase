import matplotlib.pyplot as mpl
import streamlit as st
import pandas as pd
import numpy as np

def barChart(df,x,y):
    height = 600
    if y == 'Total Disasters':
        counts = df[x].value_counts().sort_values(ascending=True)
        fig, ax = mpl.subplots(figsize=(8,max(4,len(counts)*0.3)))
        ax.barh(counts.index,counts.values,color='forestgreen',edgecolor='black')
    else:
        values = df.groupby(x)[y].sum().reset_index().sort_values(by=y,ascending=False)
        st.write(values)
        quantTuple = tuple(values[y])
        qualTuple = tuple(values[x])
        fig, ax = mpl.subplots(figsize=(8,max(4,len(qualTuple)*0.3)))
        ax.barh(qualTuple,quantTuple,color='forestgreen',edgecolor='black')
    ax.set_xlabel(f'{x}')
    ax.set_ylabel(f'{y}')
    ax.margins(y=0.005)
    fig.tight_layout()
    st.title(f'{y} by {x}')
    #with st.container(height=height):
    st.pyplot(fig)

def linePlot(df,x,y):
    if y == 'Total Disasters':
        counts = df[x].value_counts().sort_values(ascending=True)
        fig, ax = mpl.subplots()
        ax.plot(counts.index,counts.values,linestyle='-',marker='o',linewidth=2)
    else:
        #do things
        g = 1
    ax.set_xlabel(f'{x}')
    ax.set_ylabel(f'{y}')
    st.title(f'{y} by {x}')
    st.pyplot(fig)

def pieChart(df,x,y):
    # WANT TO ADD 'OTHER' CATEGORY TO PIE CHART
    if y == 'Total Disasters':
        counts = df[x].value_counts().sort_values(ascending=False)
        fig, ax = mpl.subplots()
        ax.pie(counts.values[:5],labels=counts.index[:5],autopct='%1.1f%%', shadow=True,startangle=50)
    else:
        values = df.groupby(x)[y].sum().reset_index().sort_values(by=y,ascending=False)
        st.write(values)
        quantTuple = tuple(values[y][:5])
        qualTuple = tuple(values[x][:5])
        fig,ax = mpl.subplots()
        ax.pie(quantTuple,labels=qualTuple,autopct='%1.1f%%',shadow=True,startangle=50,textprops={'fontsize':8})
    ax.axis('equal')
    st.title(f'{y} by {x}')
    st.pyplot(fig)

#Pre-Made Charts
def disastersByContinent(df):
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


