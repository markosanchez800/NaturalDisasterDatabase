import pandas as pd
import dbHelperFunctions as dhf
import sqlite3
import streamlit as st
import sqliteFunctions as sqf
import matplotFunctions as mpf

data1900_2021 = 'data/DISASTERS/1900_2021_DISASTERS.xlsx - emdat data.csv'
data1970_2021 = 'data/DISASTERS/1970-2021_DISASTERS.xlsx - emdat data.csv'

df19002021 = pd.read_csv(data1900_2021, low_memory=False)
df19702021 = pd.read_csv(data1970_2021, low_memory=False)
#Categories for Queries and Graphs
region_label = 'Region'
continent_label = 'Continent'
disaster_type_label = 'Disaster Type'
country_label = 'Country'
disaster_types = df19002021[disaster_type_label].unique()
countries = df19002021[country_label].unique()
regions = df19002021[region_label].unique()
continents = df19002021[continent_label].unique()
disaster_subgroups = df19002021['Disaster Subgroup'].unique()
years = df19002021['Year'].unique()
disaster_subtypes = df19002021['Disaster Subtype'].unique()
regions = df19002021['Region'].unique()
continents = df19002021['Continent'].unique()

dhf.cleanDataFrame(df19002021)

connection = sqlite3.connect('disasters.db')
df19002021.to_sql(name='Disasters_1900_2021', con = connection, if_exists = 'replace', index = False)
cursor = connection.cursor()

st.set_page_config(page_title='Natural Disaster Database', layout='centered')
st.title('Natural Disaster Database')
sidebar, main_content = st.columns([1,2])
# NEED TO FIGURE OUT WAY TO ALLOW FOR SPECIFIC TYPES OF CHARTS/GRAPHS
# MAYBE BUTTON FOR DIFFERENT TYPES AND A SWITCH STATEMENT?
with sidebar:
    st.header('Make a Chart/Plot')
    with st.form('make_chart_form',clear_on_submit=True):
        variableOne = st.text_input('Variable One')
        variableTwo = st.text_input('Variable Two')
        #ADD ACTUAL IMPLEMENTATION  USING MATPLOTLIB
        submit_btn = st.form_submit_with_no_rerun = st.form_submit_button('Make Chart/Graph')

        if submit_btn:
            if (variableOne and variableTwo):
                #IMPLEMENTATION HERE
                st.success("Chart Created!")
                mpf.barChart(variableOne,variableTwo)
                #st.rerun()
            else:
                st.error("Need Two Variables for Chart")

with main_content:
    st.header('Natural Disasters 1900-2021')
    st.dataframe(df19002021,use_container_width=True,hide_index=True)
    st.subheader("Make a Query:")
    with st.form('make_query_form',clear_on_submit=True):
        year1 = st.selectbox('Year:',years, index=None)
        year2 = st.selectbox('Year (Range from above input):',years, index=None)
        country = st.selectbox('Country:',countries, index=None)
        disaster_subgroup = st.selectbox('Disaster Subgroup:',disaster_subgroups, index=None)
        disaster_type = st.selectbox('Disaster Type:',disaster_types, index=None)
        disaster_subtype = st.selectbox('Disaster Sub-Type:',disaster_subtypes, index=None)
        region = st.selectbox('Region:',regions, index=None)
        continent = st.selectbox('Continent:',continents, index=None)
        query_btn = st.form_submit_with_no_rerun = st.form_submit_button('Query')
        if query_btn:
            st.success("Querying Database!")
            st.dataframe(sqf.streamlitQuery(connection,year1,year2,country,disaster_subgroup,disaster_type,disaster_subtype,region,continent))

#connection.close()
