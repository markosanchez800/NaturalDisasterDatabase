import matplotlib.pyplot as mpl
import streamlit as st

def barChart(x,y):
    #dbarChart = mpl.bar(x,y,color='forestgreen',edgecolor='lemonchiffon',width=0.6)
    fig,ax = mpl.subplots()
    ax.plot(x,y,color='forestgreen')
    st.pyplot(fig)

def lineGraph():
    return(1)


#Types of possible charts:
#Disasters by year
#Disasters by location
#Types of disasters in locations
#Fatalities by disaster type


