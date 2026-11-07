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
graphTypes = ('Bar Chart', 'Scatter Plot', 'Pie Chart', 'Line Plot', 'Pre-Made Graphs')
preMadeGraphs = ('Disasters By Country (Bar)','Disasters By Year (Bar)', 'Disasters By Continent (Pie)')
qualvariableTypes = ('Region','Country','Continent','Disaster Type','Disaster Subgroup','Disaster Subtype','Year')
quanvariableTypes = ('Total Deaths','No Injured',"Total Damages ('000 US$)",'Total Disasters')

dhf.cleanDataFrame(df19002021)

# Create SQLite database connection
connection = sqlite3.connect('disasters.db')
cursor = connection.cursor()
cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    AND name='Disasters_1900_2021'
""")
# Check if the table exists, if not, create it
table_exists = cursor.fetchone()
if table_exists is None:
    df19002021.to_sql(
        name='Disasters_1900_2021',
        con=connection,
        if_exists='fail',
        index=False
    )

st.set_page_config(page_title='Natural Disaster Database', layout='centered')
st.title('Natural Disaster Database')
sidebar, main_content = st.columns([1,2])
# Graph generation on sidebar
with sidebar:
    st.header('Make a Chart/Plot')
    graphType = st.selectbox('Graph Type:',graphTypes)
    if graphType == 'Pre-Made Graphs':
        premadeGraph = st.selectbox('Pre-Made Graphs:',preMadeGraphs)
        if st.button('Select'):
            st.session_state.premade_choice = premadeGraph
    elif graphType in graphTypes:
        variableOne = st.selectbox('Qualitative Variable:',qualvariableTypes)
        variableTwo = st.selectbox('Quantitative Variable:',quanvariableTypes)
        if st.button('Create'):
            st.session_state.create_choice = graphType
choice = st.session_state.get('premade_choice')
toCreate = st.session_state.get('create_choice')
if choice:
    match choice:
        case 'Disasters By Continent (Pie)':
            mpf.disastersByContinent(df19002021)
        case 'Disasters By Country (Bar)':
            mpf.disastersByCountry(df19002021)
        case 'Disasters By Year (Bar)':
            mpf.disastersByYear(df19002021)
        case _:
            st.warning(f'No match for {premadeGraph!r}')
if toCreate:
    match graphType:
        case 'Bar Chart':
            mpf.barChart(df19002021,variableOne,variableTwo)
        case 'Pie Chart':
            mpf.pieChart(df19002021,variableOne,variableTwo)
# Query generation on center
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
            if (sqf.streamlitQuery(connection,year1,year2,country,disaster_subgroup,disaster_type,disaster_subtype,region,continent).empty):
                st.write('Nothing found matching that query!')
            else:
                st.dataframe(sqf.streamlitQuery(connection,year1,year2,country,disaster_subgroup,disaster_type,disaster_subtype,region,continent))

st.subheader("Manage Disaster Records")

action = st.selectbox(
    "Choose an action:",
    [
        "None",
        "Add Disaster",
        "Update Disaster",
        "Delete Disaster"
    ]
)

if action == "Add Disaster":
    mpf.addDisasterStreamlit()

elif action == "Update Disaster":
    mpf.updateDisasterStreamlit()

elif action == "Delete Disaster":
    mpf.deleteDisasterStreamlit()

#connection.close()
