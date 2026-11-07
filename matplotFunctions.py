import matplotlib.pyplot as mpl
import streamlit as st
import sqliteFunctions as sf
import pandas as pd

def barChart(df,x,y):
    #CURRENTLY ONLY WORKS FOR TOTAL OCCURENCES OF X
    height = 600
    counts = df[x].value_counts().sort_values(ascending=True)
    fig, ax = mpl.subplots(figsize=(8,max(4,len(counts)*0.3)))
    ax.barh(counts.index,counts.values,color='forestgreen',edgecolor='black')
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

# add disaster
def addDisasterStreamlit():
    st.title("Add Disaster")

    with st.form("add_disaster_form"):
        # Input fields for the new disaster record
        country = st.text_input("Country")
        disaster_type = st.text_input("Disaster Type")

        year = st.number_input(
            "Start Year",
            min_value=1900,
            max_value=2100,
            step=1
        )

        total_deaths = st.number_input(
            "Total Deaths",
            min_value=0,
            step=1
        )

        submit = st.form_submit_button("Add Disaster")

        if submit:

            if country == "" or disaster_type == "":
                st.error("Please enter a country and disaster type.")

            else:
                connection = sf.beginSQLiteSession()

                row_id = sf.addDisaster(
                    connection,
                    country,
                    disaster_type,
                    int(year),
                    int(total_deaths)
                )

                sf.closeSQLiteSession(connection)

                st.success(
                    f"Disaster added successfully. Row ID: {row_id}"
                )

# delete disaster
def updateDisasterStreamlit():
    st.title("Update Disaster")

    with st.form("update_disaster_form"):
        # Input fields for the disaster record to update
        row_id = st.number_input(
            "Row ID",
            min_value=1,
            step=1
        )

        country = st.text_input("Country")

        disaster_type = st.text_input(
            "Disaster Type"
        )

        year = st.number_input(
            "Start Year",
            min_value=1900,
            max_value=2100,
            step=1
        )

        total_deaths = st.number_input(
            "Total Deaths",
            min_value=0,
            step=1
        )

        submit = st.form_submit_button(
            "Update Disaster"
        )

        if submit:

            connection = sf.beginSQLiteSession()

            rows_updated = sf.updateDisaster(
                connection,
                int(row_id),
                country,
                disaster_type,
                int(year),
                int(total_deaths)
            )

            sf.closeSQLiteSession(connection)

            if rows_updated == 1:
                st.success(
                    "Disaster updated successfully."
                )

            else:
                st.error(
                    "No disaster was found with that Row ID."
                )

# delete disaster
def deleteDisasterStreamlit():
    st.title("Delete Disaster")
    # Input field for the Row ID of the disaster record to delete
    row_id = st.number_input(
        "Row ID to Delete",
        min_value=1,
        step=1
    )

    confirm = st.checkbox(
        "I understand that this record will be permanently deleted."
    )

    if st.button("Delete Disaster"):

        if not confirm:
            st.warning(
                "Please confirm before deleting."
            )

        else:
            connection = sf.beginSQLiteSession()

            rows_deleted = sf.deleteDisaster(
                connection,
                int(row_id)
            )

            sf.closeSQLiteSession(connection)

            if rows_deleted == 1:
                st.success(
                    "Disaster deleted successfully."
                )

            else:
                st.error(
                    "No disaster was found with that Row ID."
                )

#Types of possible charts:
#Disasters by year
#Disasters by location
#Types of disasters in locations
#Fatalities by disaster type


