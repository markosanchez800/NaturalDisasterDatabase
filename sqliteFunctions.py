import sqlite3
import pandas as pd

DB_NAME = "disasters.db"

# Functions for interacting with the SQLite database
def beginSQLiteSession():
    connection = sqlite3.connect(DB_NAME)
    return connection

def streamlitQuery(connection,year1,year2,country,disaster_subgroup,disaster_type,disaster_subtype,region,continent):
    #cursor = connection.cursor()
    if (year1 and year2):
        query = """
                SELECT *
                FROM Disasters_1900_2021
                WHERE Year >= ? AND Year <= ? AND Country LIKE ? AND [Disaster Subgroup] LIKE ? AND [Disaster Type] LIKE ? AND [Disaster Subtype] LIKE ? AND Region LIKE ? AND Continent LIKE ?
                """
        params = [year1,year2,country,disaster_subgroup,disaster_type,disaster_subtype,region,continent]
        cleanedQParams = tuple('%' if p is None else p for p in params)
    if (year1 and year2 is None):
        query = """
                SELECT *
                FROM Disasters_1900_2021
                WHERE Year = ? AND Country LIKE ? AND [Disaster Subgroup] LIKE ? AND [Disaster Type] LIKE ? AND [Disaster Subtype] LIKE ? AND Region LIKE ? AND Continent LIKE ?
                """
        params = [year1,country,disaster_subgroup,disaster_type,disaster_subtype,region,continent]
        cleanedQParams = tuple('%' if p is None else p for p in params)
    if (year1 is None and year2 is None):
        query = """
                SELECT *
                FROM Disasters_1900_2021
                WHERE Country LIKE ? AND [Disaster Subgroup] LIKE ? AND [Disaster Type] LIKE ? AND [Disaster Subtype] LIKE ? AND Region LIKE ? AND Continent LIKE ?
                """
        params = [country,disaster_subgroup,disaster_type,disaster_subtype,region,continent]
        cleanedQParams = tuple('%' if p is None else p for p in params)
    if (year1 is None and year2):
        query = """
                SELECT *
                FROM Disasters_1900_2021
                WHERE Year = ? AND Country LIKE ? AND [Disaster Subgroup] LIKE ? AND [Disaster Type] LIKE ? AND [Disaster Subtype] LIKE ? AND Region LIKE ? AND Continent LIKE ?
                """
        params = [year2,country,disaster_subgroup,disaster_type,disaster_subtype,region,continent]
        cleanedQParams = tuple('%' if p is None else p for p in params)
    qdf = pd.read_sql_query(query,connection,params=cleanedQParams)
    return(qdf)


# Function to retrieve disasters by country
def getDisastersByCountry(connection, country):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT [Disaster Type], Country, [Start Year], [Total Deaths]
        FROM Disasters_1900_2021
        WHERE Country = ?
    """, (country,))

    return cursor.fetchall()

# Function to retrieve disasters by type
def getDisastersByType(connection, disaster_type):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT Country, [Disaster Type], [Start Year], [Total Deaths]
        FROM Disasters_1900_2021
        WHERE [Disaster Type] = ?
    """, (disaster_type,))

    return cursor.fetchall()

# Function to retrieve disasters by year
def getDisastersByYear(connection, year):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT Country, [Disaster Type], [Start Year], [Total Deaths]
        FROM Disasters_1900_2021
        WHERE [Start Year] = ?
    """, (year,))

    return cursor.fetchall()

#Function to retrieve total deaths by disaster type
def getTotalDeathsByType(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT [Disaster Type], SUM([Total Deaths])
        FROM Disasters_1900_2021
        GROUP BY [Disaster Type]
        ORDER BY SUM([Total Deaths]) DESC
    """)
    
    return cursor.fetchall()

# Function to retrieve the 10 deadliest disasters
def getDeadliestDisasters(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT Country, [Disaster Type], [Start Year], [Total Deaths]
        FROM Disasters_1900_2021
        ORDER BY [Total Deaths] DESC
        LIMIT 10
    """)

    return cursor.fetchall()

# Function to close the SQLite session
def closeSQLiteSession(connection):
    connection.close()
