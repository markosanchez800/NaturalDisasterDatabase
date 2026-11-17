import matplotlib.pyplot as mpl
import streamlit as st
import sqliteFunctions as sf
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
        counts = df[x].value_counts().sort_index()
        fig, ax = mpl.subplots()
        ax.plot(counts.index,counts.values,linestyle='-',marker='o',linewidth=2, color='forestgreen')
        for i in range(len(counts)):
            ax.plot(counts[i].index,counts[i].values,linestyle='-',marker='o',linewidth=2)
    else:
        values = (df.groupby(x)[y].sum().reset_index().sort_values(by=x))
        st.write(values)
        fig, ax = mpl.subplots(figsize=(8, 5))
        ax.plot(values[x], values[y], linestyle='-', marker='o', linewidth=2, color='forestgreen')
    ax.set_xlabel(f'{x}')
    ax.set_ylabel(f'{y}')
    st.title(f'{y} by {x}')
    st.pyplot(fig)

def scatterPlot(df, x, y):
    if y == 'Total Disasters':
        counts = df[x].value_counts().sort_index()
        fig, ax = mpl.subplots()
        ax.scatter(counts.index, counts.values, color='forestgreen', edgecolor='black')
    else:
        values = (df.groupby(x)[y].sum().reset_index().sort_values(by=x))
        st.write(values)
        fig, ax = mpl.subplots(figsize=(8, 5))
        ax.scatter(values[x], values[y], color='forestgreen', edgecolor='black')
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


