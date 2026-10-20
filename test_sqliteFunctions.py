# for testing the sqliteFunctions.py file
import sqliteFunctions as sf

connection = sf.beginSQLiteSession()

# Test getDisastersByCountry function
results = sf.getDisastersByCountry(
    connection,
    "United States of America"
)

for row in results:
    print(row)

sf.closeSQLiteSession(connection)