import pandas as pd
import dbHelperFunctions as dhf
import sqlite3

data1900_2021 = 'data/DISASTERS/1900_2021_DISASTERS.xlsx - emdat data.csv'
data1970_2021 = 'data/DISASTERS/1970-2021_DISASTERS.xlsx - emdat data.csv'

df19002021 = pd.read_csv(data1900_2021, low_memory=False)
df19702021 = pd.read_csv(data1970_2021, low_memory=False)
region_label = 'Region'
continent_label = 'Continent'
disaster_type_label = 'Disaster Type'
country_label = 'Country'
disaster_types = df19002021[disaster_type_label].unique()
countries = df19002021[country_label].unique()
regions = df19002021[region_label].unique()
continents = df19002021[continent_label].unique()

print(disaster_types)
print(countries)
print(regions)
print(continents)
dhf.cleanDataFrame(df19002021)
#dhf.cleanDataFrame(df19702021)
print(df19002021.columns)
#Making sure SQLite is functioning properly, practing best methods and how to query for user entry later on
connection = sqlite3.connect('disasters.db')
df19002021.to_sql(name='Disasters_1900_2021', con = connection, if_exists = 'replace', index = False)
cursor = connection.cursor()
cursor.execute("SELECT [Disaster Type], Country, [Start Year], [Total Deaths] FROM Disasters_1900_2021 WHERE Country = ?",("Serbia",))
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.close()

