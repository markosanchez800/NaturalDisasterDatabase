import sqlite3

DB_NAME = "disasters.db"

# Functions for interacting with the SQLite database
def beginSQLiteSession():
    connection = sqlite3.connect(DB_NAME)
    return connection

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

# Function to close the SQLite session
def closeSQLiteSession(connection):
    connection.close()

