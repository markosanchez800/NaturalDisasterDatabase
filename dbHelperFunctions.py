import pandas as pd

def cleanDataFrame(df):
    print("Null Value Count:")
    print(df.isnull().sum())
    print("Duplicate Row Count:")
    print(df.duplicated().sum())
    df.drop_duplicates(inplace=True)
    df.drop(columns=['Dis No', 'Adm Level', 'Admin1 Code', 'Admin2 Code', "Reconstruction Costs ('000 US$)"], errors='ignore', inplace=True)

def getDfInfo(df):
    print(df.info())
    print(df.describe())
    print(df.shape)