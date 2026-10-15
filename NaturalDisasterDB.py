import pandas as pd

data1900_2021 = 'data/DISASTERS/1900_2021_DISASTERS.xlsx - emdat data.csv'
data1970_2021 = 'data/DISASTERS/1970-2021_DISASTERS.xlsx - emdat data.csv'

df19002021 = pd.read_csv(data1900_2021, low_memory=False)
df19702021 = pd.read_csv(data1970_2021, low_memory=False)

disaster_type_label = 'Disaster Type'
disaster_types = df19002021[disaster_type_label].unique()
print(disaster_types)

#print(df19002021.info())